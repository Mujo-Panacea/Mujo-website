#!/usr/bin/env python3
"""
Migrate WordPress posts from docs/audit/posts-raw.json to src/content/posts/*.mdx.

- Strips Divi builder shortcodes (`[et_pb_*]`).
- Decodes HTML entities.
- Converts remaining HTML to Markdown via markdownify.
- Extracts image URLs, rewrites them to local paths under /images/posts/<slug>/,
  and returns a manifest so a separate step can download the assets.
- Applies the sitemap.md mapping from post categories to (blog | news | evidence).

Run: python3 scripts/migrate_posts.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from markdownify import markdownify

ROOT = Path(__file__).resolve().parents[1]
POSTS_JSON = ROOT / "docs" / "audit" / "posts-raw.json"
CATEGORIES_JSON = ROOT / "docs" / "audit" / "categories-raw.json"
MEDIA_JSON = ROOT / "docs" / "audit" / "media-raw.json"
OUT_DIR = ROOT / "src" / "content" / "posts"
MEDIA_MANIFEST = ROOT / "docs" / "audit" / "media-manifest.json"

# Category name → collection category. Everything with no News/Evidence tag is Blog.
CATEGORY_MAP = {
    "News": "news",
    "Evidence": "evidence",
}

# Divi shortcode stripper. Divi wraps everything in [et_pb_*] ... [/et_pb_*].
DIVI_RE = re.compile(r"\[/?et_pb_[^\]]*\]")
# Other WP shortcodes we don't care about
GENERIC_SHORTCODE_RE = re.compile(r"\[/?(caption|gallery|embed|audio|video|playlist)[^\]]*\]")
# Divi image shortcode — matches straight or curly quotes around src
ET_PB_IMAGE_RE = re.compile(r"\[et_pb_image[^\]]*?src=[\"”“]([^\"”“]+)[\"”“][^\]]*?\]")
# Divi video shortcode — same idea, we'll drop to a plain link
ET_PB_VIDEO_RE = re.compile(r"\[et_pb_video[^\]]*?src=[\"”“]([^\"”“]+)[\"”“][^\]]*?\]")


def convert_divi_images(raw: str) -> str:
    """Convert [et_pb_image src="..."] shortcodes to plain <img> tags so markdownify
    turns them into normal ![alt](url) references. Runs before the Divi wholesale strip."""
    raw = ET_PB_IMAGE_RE.sub(lambda m: f'<img src="{m.group(1)}" alt="" />', raw)
    raw = ET_PB_VIDEO_RE.sub(lambda m: f'<p><a href="{m.group(1)}">Watch video</a></p>', raw)
    return raw


def clean_html(raw: str) -> str:
    """Decode entities, extract Divi images, then remove all remaining WP/Divi shortcodes."""
    decoded = html.unescape(raw or "")
    decoded = convert_divi_images(decoded)
    decoded = DIVI_RE.sub("", decoded)
    decoded = GENERIC_SHORTCODE_RE.sub("", decoded)
    return decoded


def choose_category(post_categories: list[int], id_to_name: dict[int, str]) -> str:
    names = {id_to_name.get(cid, "") for cid in post_categories}
    if "News" in names:
        return "news"
    if "Evidence" in names:
        return "evidence"
    return "blog"


def choose_tags(post_categories: list[int], id_to_name: dict[int, str]) -> list[str]:
    """Return topical categories (Frozen Shoulder, Shoulder Impingement, etc.) as tags,
    dropping the routing ones (News/Blog/Evidence/education) already captured elsewhere."""
    drop = {"News", "Blog", "Evidence", "education"}
    return sorted({id_to_name[cid] for cid in post_categories if id_to_name.get(cid) and id_to_name[cid] not in drop})


def extract_images(markdown: str, slug: str) -> tuple[str, list[dict]]:
    """Find every ![alt](url) with an mujofitness.com URL, rewrite to /images/posts/<slug>/<basename>,
    return manifest entries so the downloader can fetch them."""
    manifest: list[dict] = []

    def replace(match: re.Match) -> str:
        alt = match.group(1)
        url = match.group(2)
        parsed = urlparse(url)
        if "mujofitness.com" not in parsed.netloc:
            return match.group(0)  # external image, leave alone
        basename = Path(parsed.path).name
        local_path = f"/images/posts/{slug}/{basename}"
        manifest.append({"source": url, "local": local_path, "slug": slug})
        return f"![{alt}]({local_path})"

    rewritten = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, markdown)
    return rewritten, manifest


def to_mdx(post: dict, id_to_name: dict[int, str], media_by_id: dict[int, dict]) -> tuple[str, list[dict]]:
    slug = post["slug"]
    title = html.unescape(post["title"]["rendered"]).strip()
    excerpt_raw = clean_html(post.get("excerpt", {}).get("rendered", "") or "")
    excerpt_md = markdownify(excerpt_raw, heading_style="ATX").strip()
    # Excerpt: strip markdown, one paragraph, cap at 220 chars.
    excerpt_plain = re.sub(r"\s+", " ", re.sub(r"[*#_>`]", "", excerpt_md)).strip()
    if len(excerpt_plain) > 220:
        excerpt_plain = excerpt_plain[:217].rstrip() + "…"

    body_html = clean_html(post["content"]["rendered"])
    body_md = markdownify(body_html, heading_style="ATX", bullets="-", code_language="").strip()
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)
    # MDX 3 treats `<` as JSX. Convert Markdown autolinks `<https://...>` and
    # `<foo@bar>` to proper `[url](url)` form so MDX doesn't try to parse them as tags.
    body_md = re.sub(
        r"<(https?://[^>\s]+)>",
        lambda m: f"[{m.group(1)}]({m.group(1)})",
        body_md,
    )
    body_md = re.sub(
        r"<([\w.+-]+@[\w.-]+\.[A-Za-z]{2,})>",
        lambda m: f"[{m.group(1)}](mailto:{m.group(1)})",
        body_md,
    )
    # Strip stray HTML comments and empty <br/> tags that markdownify sometimes leaves.
    body_md = re.sub(r"<!--.*?-->", "", body_md, flags=re.DOTALL)
    # Escape bare `<` characters that MDX would otherwise try to parse as JSX tags
    # (e.g. "p<0.05", "temp <5°C"). Leave real tags/components/HTML alone.
    body_md = re.sub(r"<(?![a-zA-Z/!])", r"\\<", body_md)
    body_md, manifest = extract_images(body_md, slug)

    # Featured image (WordPress hero) — separate from body images
    featured_id = post.get("featured_media", 0)
    hero_manifest_entry = None
    hero_local = None
    if featured_id and featured_id in media_by_id:
        media = media_by_id[featured_id]
        hero_url = media.get("source_url", "")
        if hero_url:
            hero_basename = Path(urlparse(hero_url).path).name
            hero_local = f"/images/posts/{slug}/hero-{hero_basename}"
            hero_manifest_entry = {"source": hero_url, "local": hero_local, "slug": slug, "hero": True}
            manifest.append(hero_manifest_entry)

    published_date = (post.get("date") or "")[:10]
    modified_date = (post.get("modified") or "")[:10]
    category = choose_category(post.get("categories") or [], id_to_name)
    tags = choose_tags(post.get("categories") or [], id_to_name)

    # Old content — flag anything published before 2020 as archived so the reader sees it upfront.
    archived = published_date < "2020-01-01"

    frontmatter_lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"description: {json.dumps(excerpt_plain or title, ensure_ascii=False)}",
        f"publishedDate: {published_date}",
    ]
    if modified_date and modified_date != published_date:
        frontmatter_lines.append(f"updatedDate: {modified_date}")
    frontmatter_lines.append(f"category: {category}")
    if tags:
        frontmatter_lines.append(f"tags: {json.dumps(tags, ensure_ascii=False)}")
    frontmatter_lines.append(f"author: \"MUJO Panacea\"")
    if hero_local:
        frontmatter_lines.append(f"heroImage: {json.dumps(hero_local)}")
    if archived:
        frontmatter_lines.append("archived: true")
    frontmatter_lines.append(f"legacyId: {post.get('id')}")
    frontmatter_lines.append(f"legacyUrl: {json.dumps(post.get('link', ''), ensure_ascii=False)}")
    frontmatter_lines.append("---")

    return "\n".join(frontmatter_lines) + "\n\n" + body_md + "\n", manifest


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cats = json.loads(CATEGORIES_JSON.read_text())
    id_to_name = {c["id"]: c["name"] for c in cats}
    media = json.loads(MEDIA_JSON.read_text()) if MEDIA_JSON.exists() else []
    media_by_id = {m["id"]: m for m in media}

    posts = json.loads(POSTS_JSON.read_text())
    posts.sort(key=lambda p: p.get("date", ""))

    # Delete the seed post so it doesn't co-exist with migrated content.
    seed = OUT_DIR / "hello-world.mdx"
    if seed.exists():
        seed.unlink()
        print(f"removed seed post: {seed.name}")

    all_manifest: list[dict] = []
    for post in posts:
        slug = post["slug"]
        mdx, manifest = to_mdx(post, id_to_name, media_by_id)
        (OUT_DIR / f"{slug}.mdx").write_text(mdx, encoding="utf-8")
        all_manifest.extend(manifest)
        print(f"wrote {slug}.mdx ({post.get('date', '')[:10]}, {len(manifest)} images)")

    MEDIA_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MEDIA_MANIFEST.write_text(json.dumps(all_manifest, indent=2), encoding="utf-8")
    print(f"\nWrote {len(posts)} posts.")
    print(f"Wrote media manifest ({len(all_manifest)} images) to {MEDIA_MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

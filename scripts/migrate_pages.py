#!/usr/bin/env python3
"""
Migrate retained WordPress pages to MDX under src/pages/.

Strategy:
- Condition pages (frozen shoulder, impingement, instability, upper back/neck) —
  educational content that's largely evergreen; migrate + prefix a review banner.
- Everything else (home, technology, about, faqs, contact, legal) —
  write a shell with a placeholder body. The extracted WP content is preserved
  under docs/migrations/pages/ for Gerard's editorial rewrite pass.

Run: python3 scripts/migrate_pages.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from markdownify import markdownify

ROOT = Path(__file__).resolve().parents[1]
PAGES_JSON = ROOT / "docs" / "audit" / "pages-raw.json"
MIGRATION_REF_DIR = ROOT / "docs" / "migrations" / "pages"
PAGES_OUT = ROOT / "src" / "pages"

# Match Divi and other WP shortcodes
DIVI_RE = re.compile(r"\[/?et_pb_[^\]]*\]")
GENERIC_SHORTCODE_RE = re.compile(r"\[/?(caption|gallery|embed|audio|video|playlist)[^\]]*\]")
ET_PB_IMAGE_RE = re.compile(r"\[et_pb_image[^\]]*?src=[\"”“]([^\"”“]+)[\"”“][^\]]*?\]")


def wp_to_markdown(raw: str) -> str:
    """Strip Divi and WP shortcodes, convert to markdown."""
    decoded = html.unescape(raw or "")
    decoded = ET_PB_IMAGE_RE.sub(lambda m: f'<img src="{m.group(1)}" alt="" />', decoded)
    decoded = DIVI_RE.sub("", decoded)
    decoded = GENERIC_SHORTCODE_RE.sub("", decoded)
    md = markdownify(decoded, heading_style="ATX", bullets="-", code_language="").strip()
    md = re.sub(r"\n{3,}", "\n\n", md)
    # MDX safety: escape autolinks and bare `<`.
    md = re.sub(r"<(https?://[^>\s]+)>", lambda m: f"[{m.group(1)}]({m.group(1)})", md)
    md = re.sub(r"<([\w.+-]+@[\w.-]+\.[A-Za-z]{2,})>", lambda m: f"[{m.group(1)}](mailto:{m.group(1)})", md)
    md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)
    md = re.sub(r"<(?![a-zA-Z/!])", r"\\<", md)
    return md


def pages_by_slug(pages: list[dict]) -> dict[tuple[int | None, str], dict]:
    """Index pages by (parent_id, slug) since some slugs are reused across parents."""
    return {(p.get("parent") or None, p["slug"]): p for p in pages}


def dump_reference(slug: str, sources: list[dict]) -> None:
    """Write the cleaned markdown of every source page to docs/migrations/pages/<slug>.md."""
    MIGRATION_REF_DIR.mkdir(parents=True, exist_ok=True)
    parts = [f"# Legacy content for `{slug}`", ""]
    for src in sources:
        parts.append(f"## From {src['link']}")
        parts.append(f"_Title: {html.unescape(src['title']['rendered'])}_")
        parts.append("")
        parts.append(wp_to_markdown(src["content"]["rendered"]))
        parts.append("\n---\n")
    (MIGRATION_REF_DIR / f"{slug}.md").write_text("\n".join(parts), encoding="utf-8")


def write_mdx_page(
    path_parts: list[str],
    title: str,
    description: str,
    body: str,
    review_note: str | None = None,
) -> None:
    """Write an MDX page at src/pages/<path>.mdx."""
    outfile = PAGES_OUT.joinpath(*path_parts).with_suffix(".mdx")
    outfile.parent.mkdir(parents=True, exist_ok=True)

    frontmatter = [
        "---",
        "layout: ../layouts/PageLayout.astro" if len(path_parts) == 1 else f"layout: {'../' * len(path_parts)}layouts/PageLayout.astro",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "---",
    ]

    banner = ""
    if review_note:
        banner = (
            "import ReviewBanner from '"
            + ("../" * len(path_parts))
            + "components/ReviewBanner.astro';\n\n"
            + f"<ReviewBanner>{review_note}</ReviewBanner>\n\n"
        )

    outfile.write_text("\n".join(frontmatter) + "\n\n" + banner + body + "\n", encoding="utf-8")


# ─── Migration plan ────────────────────────────────────────────────────────────

CONDITION_MIGRATIONS = [
    {
        "slug": "frozen-shoulder",
        "path": ("treatments", "frozen-shoulder"),
        "title": "Frozen Shoulder",
        "description": "Frozen shoulder — symptoms, diagnosis, and how MUJO supports guided rehabilitation.",
        "sources": [
            (None, "treatments"),  # will be overridden by parent-child resolution below
        ],
    },
    {
        "slug": "shoulder-impingement",
        "path": ("treatments", "shoulder-impingement"),
        "title": "Shoulder Impingement",
        "description": "Shoulder impingement — symptoms, diagnosis, and how MUJO supports guided rehabilitation.",
    },
    {
        "slug": "shoulder-instability",
        "path": ("treatments", "shoulder-instability"),
        "title": "Shoulder Instability",
        "description": "Shoulder instability — symptoms, diagnosis, and how MUJO supports guided rehabilitation.",
    },
    {
        "slug": "upper-back-and-neck-pain",
        "path": ("treatments", "upper-back-and-neck-pain"),
        "title": "Upper Back and Neck Pain",
        "description": "Upper back and neck pain — symptoms, diagnosis, and how MUJO supports guided rehabilitation.",
    },
]

# For each condition, sources are: /treatments/<slug> (WP page under 432) + /research/conditions/<matching-slug>
CONDITION_SOURCE_MAP = {
    "frozen-shoulder": ["frozen-shoulder", "frozen-shoulder-contracture-syndrome"],
    "shoulder-impingement": ["shoulder-impingement", "shoulder-impingement-syndrome"],
    "shoulder-instability": ["shoulder-instability"],
    "upper-back-and-neck-pain": ["upper-back-and-neck-pain", "upper-back-and-neck-pain"],  # both parents have same slug
}


SHELL_PAGES = [
    {
        "path": ("technology",),
        "title": "Technology",
        "description": "The MUJO shoulder rehabilitation system — hardware, software, and clinical data.",
        "wp_slug": "technology",
        "wp_parent": None,
        "review_note": "This page will be rewritten in Phase 3 to reflect the current Mujo 1.5 hardware baseline and the Mujo 2.0 KTP programme.",
    },
    {
        "path": ("technology", "dashboard-and-predictive-model"),
        "title": "Dashboard and Predictive Model",
        "description": "The MUJO clinician dashboard and predictive analytics — a future offering under the Mujo 2.0 programme.",
        "wp_slug": "dashboard-and-predictive-model",
        "wp_parent_slug": "technology",
        "review_note": "Language shifts from \"we have this\" to \"we are building this.\" Aligns with the Mujo 2.0 roadmap. Regulatory-safe wording required — no clinical or diagnostic claims until product is on-market.",
    },
    {
        "path": ("treatments",),
        "title": "Treatments",
        "description": "Shoulder conditions treated with MUJO — frozen shoulder, impingement, instability, upper back and neck pain.",
        "wp_slug": "treatments",
        "wp_parent": None,
        "review_note": "Landing page. Editorial pass needed to reflect current product state and audiences.",
    },
    {
        "path": ("faqs",),
        "title": "FAQs",
        "description": "Frequently asked questions about MUJO — the device, the pilot programme, clinical use, and how to get in touch.",
        "wp_slug": "faqs",
        "wp_parent": None,
        "review_note": "Rewrite: every answer should end with a clear path to contact us. Retire questions that no longer apply; add questions specific to the 1.5 pilot and 2.0 programme.",
    },
    {
        "path": ("about", "index"),
        "title": "About",
        "description": "MUJO Panacea — a clinically grounded shoulder rehabilitation platform mid-way through the 2.0 KTP programme.",
        "wp_slug": "about-us",
        "wp_parent": None,
        "review_note": "Rewrite to reflect the current company posture: MUJO Panacea, the KTP programme, regulatory direction, and the 1.5/2.0 product roadmap.",
    },
    {
        "path": ("about", "team"),
        "title": "Team",
        "description": "The MUJO Panacea team.",
        "wp_slug": None,  # rebuild from scratch — new team
        "review_note": "Rebuild around current team: Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), Jeff McBride. Bios and photos to be supplied by Gerard.",
    },
    {
        "path": ("contact",),
        "title": "Contact",
        "description": "Get in touch with MUJO Panacea.",
        "wp_slug": "contact",
        "wp_parent": None,
        "review_note": "Netlify Forms integration to be added in the next commit.",
    },
    {
        "path": ("privacy",),
        "title": "Privacy Policy",
        "description": "MUJO Panacea privacy policy — how we handle personal data.",
        "wp_slug": "privacy-policy",
        "wp_parent": None,
        "review_note": "Legal review required before cutover. Must reflect current data flows (contact form intake, any analytics decision, tablet/backend data if referenced).",
    },
    {
        "path": ("terms",),
        "title": "Terms and Conditions",
        "description": "MUJO Panacea terms and conditions.",
        "wp_slug": "terms-and-conditions",
        "wp_parent": None,
        "review_note": "Legal review required before cutover.",
    },
]


def main() -> None:
    pages = json.loads(PAGES_JSON.read_text())
    idx = pages_by_slug(pages)
    # Also index by slug alone (fallback when parent lookup is ambiguous)
    by_slug: dict[str, list[dict]] = {}
    for p in pages:
        by_slug.setdefault(p["slug"], []).append(p)

    # 1. Condition pages — migrate merged content with a review banner.
    for cfg in CONDITION_MIGRATIONS:
        slug = cfg["slug"]
        source_slugs = CONDITION_SOURCE_MAP[slug]
        sources: list[dict] = []
        seen_ids: set[int] = set()
        for s_slug in source_slugs:
            for candidate in by_slug.get(s_slug, []):
                if candidate["id"] not in seen_ids:
                    sources.append(candidate)
                    seen_ids.add(candidate["id"])
        if not sources:
            print(f"skip condition {slug}: no source pages found")
            continue

        # Pick the longer source as the canonical body; append other sources below a divider.
        sources.sort(key=lambda s: len(s["content"]["rendered"]), reverse=True)
        canonical = sources[0]
        extras = sources[1:]

        body_parts = [wp_to_markdown(canonical["content"]["rendered"])]
        for extra in extras:
            body_parts.append(f"\n\n---\n\n## Additional legacy content — merged from {extra['link']}\n\n")
            body_parts.append(wp_to_markdown(extra["content"]["rendered"]))

        review = "Educational content migrated from the legacy site. Review for accuracy and update where clinical language or product references are out of date."
        write_mdx_page(
            list(cfg["path"]),
            cfg["title"],
            cfg["description"],
            "\n\n".join(body_parts),
            review_note=review,
        )
        dump_reference(slug, sources)
        print(f"wrote condition {'/'.join(cfg['path'])} (from {len(sources)} source(s))")

    # 2. Shell pages.
    for cfg in SHELL_PAGES:
        source: dict | None = None
        if cfg["wp_slug"]:
            candidates = by_slug.get(cfg["wp_slug"], [])
            parent_slug = cfg.get("wp_parent_slug")
            if parent_slug:
                parent = next((p for p in pages if p["slug"] == parent_slug and not p["parent"]), None)
                if parent:
                    source = next((c for c in candidates if c["parent"] == parent["id"]), None)
            else:
                # Prefer the top-level page (parent==0) if there are multiple
                source = next((c for c in candidates if not c["parent"]), None) or (candidates[0] if candidates else None)

        body = "{/* Content to be authored during Phase 3 editorial pass. */}\n\nContent for this page is being written as part of the Phase 3 editorial pass. The reference material from the legacy site (if any) lives at `docs/migrations/pages/`."
        if source:
            dump_reference(source["slug"] + ("__" + cfg["path"][-1] if source["slug"] != cfg["path"][-1] else ""), [source])

        # Sanitise the path — Astro treats `index.mdx` as the directory root.
        path_parts = list(cfg["path"])
        write_mdx_page(
            path_parts,
            cfg["title"],
            cfg["description"],
            body,
            review_note=cfg["review_note"],
        )
        print(f"wrote shell {'/'.join(path_parts)}")


if __name__ == "__main__":
    main()

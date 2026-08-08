#!/usr/bin/env python3
"""
Post-migration cleanup on src/content/posts/*.mdx:

1. Fix descriptions that begin with `![](url)` image markdown — strip the
   image, use the first meaningful sentence of the body instead.
2. Strip absolute `mujofitness.com` URLs from the body. Where the target
   is another post that survived the reshape, rewrite as an internal link
   (e.g. legacy `/news/2016/11/30/positive-results-reported-clinical-study/`
   → `/evidence/positive-results-reported-clinical-study/`).
3. Where a link points to a killed URL, leave the anchor text as plain
   emphasis (drop the link) — no dangling internal 404s and no traffic
   sent back to the old site.

Run: python3 scripts/clean_posts.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "src" / "content" / "posts"

# Slugs that survived the reshape. Anything else gets its link dropped.
SURVIVING_EVIDENCE = {
    "tried-and-tested",
    "positive-results-reported-clinical-study",
    "upper-quadrant-motor-control-training-mujo-reduce-fall-rates-elderly",
    "mujo-interviews-dr-niels-peek-university-manchester",
    "coventry-university-evaluates-mujo-devices",
    "clinical-feasibility-study-begins-royal-national-orthopaedic-hospital",
    "circlebedfordshire-msk-service-joins-innovate-uk-study",
    "installation-royal-national-orthopaedic-hospital-nhs-trust",
    "installation-english-institute-sport-lilleshall-national-sports-centre",
    "english-institute-of-sport-adopts-mujo",
    "wasps-rugby-use-mujo-system-for-post-op-shoulder-dislocation-rehabilitation",
    "mujo-supplies-leading-dutch-workmans-compensation-training-centre-artros-healthfocus",
    "mujo-available-gb-weightlifting-affiliate-iron-club-vauxhall",
    "ratio-medical-training-ag-appointed-swiss-representative",
    "mujo-wins-innovate-uk-funding-digital-health-connected-hospital",
    "mujo-showcases-connected-devices-innovate-2015-registers-mhra",
    "mujo-patent-approved-united-states",
    "mujo-achieves-fda-listing-for-its-connected-health-devices",
}

SURVIVING_RESOURCES = {
    "anatomy-of-the-shoulder-part-1",
    "anatomy-of-the-shoulder-part-2-ligaments-and-capsules",
    "anatomy-of-the-shoulder-part-3-muscular-structures",
    "7-home-based-exercises-to-help-a-frozen-shoulder",
    "mujo-exercises-for-shoulder-impingement-syndrome",
    "5-exercises-to-help-correct-shoulder-impingement-syndrome",
}


def slug_from_legacy_url(url: str) -> tuple[str, str] | None:
    """Return (category, slug) if the URL is a legacy WP post URL, else None."""
    m = re.search(
        r"mujofitness\.com/(?:blog|news|evidence)/\d{4}/\d{2}/\d{2}/([a-z0-9-]+)/?",
        url,
    )
    if not m:
        return None
    slug = m.group(1)
    if slug in SURVIVING_EVIDENCE:
        return ("evidence", slug)
    if slug in SURVIVING_RESOURCES:
        return ("resources", slug)
    return None


def strip_or_rewrite_legacy_link(match: re.Match) -> str:
    """
    Given a markdown link `[text](url)`, rewrite it to an internal URL if the
    target post survived, drop the link (leaving plain text) if it didn't,
    or leave the link untouched if it doesn't point at mujofitness.com.
    """
    text = match.group(1)
    url = match.group(2)
    if "mujofitness.com" not in url:
        return match.group(0)
    resolved = slug_from_legacy_url(url)
    if resolved:
        cat, slug = resolved
        return f"[{text}](/{cat}/{slug}/)"
    # Also handle bare non-post URLs (e.g. /technology/) — rewrite to internal.
    bare = re.search(r"mujofitness\.com(/[^\s)]+)?", url)
    if bare and bare.group(1):
        path = bare.group(1).rstrip("/") + "/"
        # A few known reshape destinations
        remap = {
            "/technology/": "/technology/",
            "/evidence/": "/evidence/",
            "/contact/": "/contact/",
        }
        target = remap.get(path)
        if target:
            return f"[{text}]({target})"
    # Unknown target — drop the link, keep the text.
    return text


def clean_body(body: str) -> str:
    # Rewrite markdown links first
    body = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", strip_or_rewrite_legacy_link, body)
    # Then drop any lingering bare URLs to mujofitness.com
    body = re.sub(r"https?://(?:www\.)?mujofitness\.com/\S+", "", body)
    body = re.sub(r"[ \t]+\n", "\n", body)
    return body


LEADING_IMAGE = re.compile(r"^\s*!\[[^\]]*\]\([^)]+\)\s*")


def clean_description(description: str, body_md: str) -> str:
    # Strip a leading `![](url)` if the description opens with one.
    cleaned = LEADING_IMAGE.sub("", description).strip()
    if len(cleaned) >= 40:
        return cleaned
    # Description became too thin — regenerate from body.
    plain = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", body_md)  # drop images
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain)  # unwrap links
    plain = re.sub(r"[*#_>`\\]+", "", plain)                # strip md syntax
    plain = re.sub(r"\s+", " ", plain).strip()
    if len(plain) > 220:
        plain = plain[:217].rstrip() + "…"
    return plain or cleaned


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n"), text[end + 5 :]


def main() -> None:
    fixed_desc = fixed_links = 0
    for path in sorted(POSTS_DIR.glob("*.mdx")):
        text = path.read_text(encoding="utf-8")
        parts = split_frontmatter(text)
        if not parts:
            print(f"WARN: no frontmatter in {path.name}")
            continue
        fm_raw, body = parts

        new_body = clean_body(body)

        # Extract description line, clean it.
        desc_match = re.search(r'^description:\s*(?:"((?:[^"\\]|\\.)*)"|(.*))\s*$', fm_raw, re.MULTILINE)
        if not desc_match:
            print(f"WARN: no description line in {path.name}")
            fm_new = fm_raw
        else:
            existing = desc_match.group(1) or desc_match.group(2) or ""
            # `\"` inside a quoted YAML string is the only escape we care about;
            # do not decode UTF-8 bytes back through unicode_escape (that would
            # mangle characters like `…` in already-well-formed UTF-8).
            existing = existing.replace('\\"', '"').replace("\\\\", "\\")
            new_desc = clean_description(existing, new_body)
            if new_desc != existing:
                fixed_desc += 1
                # Re-quote as JSON-ish string for YAML safety.
                escaped = new_desc.replace("\\", "\\\\").replace('"', '\\"')
                fm_new = re.sub(
                    r'^description:.*$',
                    f'description: "{escaped}"',
                    fm_raw,
                    count=1,
                    flags=re.MULTILINE,
                )
            else:
                fm_new = fm_raw

        if new_body != body:
            fixed_links += 1

        path.write_text(f"---\n{fm_new}\n---\n{new_body}", encoding="utf-8")

    print(f"descriptions fixed: {fixed_desc}")
    print(f"bodies with links stripped/rewritten: {fixed_links}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Reclassify migrated posts per the 2026-08-06 IA change.

- News + blog collapse into two categories: `evidence` and `resources`.
- Killed posts get deleted; their image folders are kept in case content
  moves to /athletes/ or elsewhere in future.
- Every surviving post has its `category` frontmatter rewritten in place.

Run: python3 scripts/reclassify_posts.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "src" / "content" / "posts"

# slug → new category ("evidence" | "resources" | None means KILL)
CLASSIFICATION: dict[str, str | None] = {
    # ─── EVIDENCE (18) — studies, trials, device-in-use, milestone press ─────
    "tried-and-tested": "evidence",
    "positive-results-reported-clinical-study": "evidence",
    "upper-quadrant-motor-control-training-mujo-reduce-fall-rates-elderly": "evidence",
    "mujo-interviews-dr-niels-peek-university-manchester": "evidence",
    "coventry-university-evaluates-mujo-devices": "evidence",
    "clinical-feasibility-study-begins-royal-national-orthopaedic-hospital": "evidence",
    "circlebedfordshire-msk-service-joins-innovate-uk-study": "evidence",
    "installation-royal-national-orthopaedic-hospital-nhs-trust": "evidence",
    "installation-english-institute-sport-lilleshall-national-sports-centre": "evidence",
    "english-institute-of-sport-adopts-mujo": "evidence",
    "wasps-rugby-use-mujo-system-for-post-op-shoulder-dislocation-rehabilitation": "evidence",
    "mujo-supplies-leading-dutch-workmans-compensation-training-centre-artros-healthfocus": "evidence",
    "mujo-available-gb-weightlifting-affiliate-iron-club-vauxhall": "evidence",
    "ratio-medical-training-ag-appointed-swiss-representative": "evidence",
    "mujo-wins-innovate-uk-funding-digital-health-connected-hospital": "evidence",
    "mujo-showcases-connected-devices-innovate-2015-registers-mhra": "evidence",
    "mujo-patent-approved-united-states": "evidence",
    "mujo-achieves-fda-listing-for-its-connected-health-devices": "evidence",

    # ─── RESOURCES (6) — evergreen educational content ───────────────────────
    "anatomy-of-the-shoulder-part-1": "resources",
    "anatomy-of-the-shoulder-part-2-ligaments-and-capsules": "resources",
    "anatomy-of-the-shoulder-part-3-muscular-structures": "resources",
    "7-home-based-exercises-to-help-a-frozen-shoulder": "resources",
    "mujo-exercises-for-shoulder-impingement-syndrome": "resources",
    "5-exercises-to-help-correct-shoulder-impingement-syndrome": "resources",

    # ─── KILL (18) — award shortlists, thin generic articles, sports rehashes ─
    "mujo-exhibits-bess-annual-scientific-meeting": None,
    "mujo-shortlisted-british-engineering-excellence-awards": None,
    "iet-innovation-awards-2013-finalists-announced": None,
    "mujo-attends-eusser-international-shoulder-symposium-2014": None,
    "mujo-presents-connected-plans-digital-health-pit-stop-week": None,
    "mujo-shortlisted-major-sports-technology-award": None,
    "mujo-pitches-inaugural-angels-medcity-event": None,
    "mujo-awarded-best-exhibitor-formula-1-advances-healthcare-event": None,
    "mujo-joins-founding-corporate-member-imperial-college-medtech-links": None,
    "pitchpalace-5-0-entrepreneurs-announced": None,
    "accelerating-british-innovation-cross-industry-collaboration": None,
    "brain-is-constantly-changing-motor-control-learning": None,
    "shoulder-pain-night": None,
    "top-rotator-cuff-exercises-to-fix-shoulder-pain": None,
    "best-exercises-frozen-shoulder-contracture-syndrome": None,
    "nfl-shoulder-injuries-and-mujo": None,
    "baseball-gird-shoulder-other-injuries-mujo": None,
    "how-to-help-reduce-shoulder-pain-when-raising-your-arm": None,
}


def main() -> None:
    existing = {p.stem: p for p in POSTS_DIR.glob("*.mdx")}
    classified = set(CLASSIFICATION)

    missing = classified - set(existing)
    extra = set(existing) - classified
    if missing:
        print(f"WARN: {len(missing)} slugs in classification not found on disk:", file=sys.stderr)
        for s in sorted(missing):
            print(f"  {s}", file=sys.stderr)
    if extra:
        print(f"WARN: {len(extra)} slugs on disk not in classification:", file=sys.stderr)
        for s in sorted(extra):
            print(f"  {s}", file=sys.stderr)

    kept_evidence = kept_resources = killed = 0
    for slug, new_category in CLASSIFICATION.items():
        path = existing.get(slug)
        if not path:
            continue
        if new_category is None:
            path.unlink()
            killed += 1
            print(f"killed {slug}")
            continue

        text = path.read_text(encoding="utf-8")
        new_text = re.sub(
            r"^category:\s*\S+\s*$",
            f"category: {new_category}",
            text,
            count=1,
            flags=re.MULTILINE,
        )
        if new_text == text:
            print(f"WARN: no category line rewritten in {slug}", file=sys.stderr)
        else:
            path.write_text(new_text, encoding="utf-8")

        if new_category == "evidence":
            kept_evidence += 1
        else:
            kept_resources += 1

    print(f"\nevidence={kept_evidence}  resources={kept_resources}  killed={killed}")
    print(f"total_input={len(CLASSIFICATION)}  total_on_disk_after={kept_evidence + kept_resources}")


if __name__ == "__main__":
    main()

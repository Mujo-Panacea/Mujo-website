#!/usr/bin/env python3
"""Download every image in docs/audit/media-manifest.json to public/images/posts/<slug>/."""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "audit" / "media-manifest.json"
PUBLIC = ROOT / "public"


def main() -> None:
    entries = json.loads(MANIFEST.read_text())
    total = len(entries)
    ok = skipped = failed = 0

    for i, e in enumerate(entries, 1):
        source = e["source"]
        local = e["local"].lstrip("/")
        dest = PUBLIC / local
        dest.parent.mkdir(parents=True, exist_ok=True)

        if dest.exists() and dest.stat().st_size > 0:
            skipped += 1
            continue

        try:
            req = urllib.request.Request(
                source,
                headers={"User-Agent": "MujoWebsiteMigration/1.0"},
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                dest.write_bytes(resp.read())
            ok += 1
            print(f"[{i}/{total}] ok  {local}")
        except Exception as ex:
            failed += 1
            print(f"[{i}/{total}] FAIL {local}: {ex}", file=sys.stderr)
        # be polite
        time.sleep(0.05)

    print(f"\ndownloaded={ok}  skipped={skipped}  failed={failed}  total={total}")


if __name__ == "__main__":
    main()

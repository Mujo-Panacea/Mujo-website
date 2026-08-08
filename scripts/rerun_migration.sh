#!/usr/bin/env bash
# Rebuild the posts corpus from scratch: re-migrate from raw JSON,
# then re-run the cleanup pass. Idempotent — safe to run repeatedly.
set -euo pipefail
python3 scripts/migrate_posts.py
python3 scripts/reclassify_posts.py
python3 scripts/clean_posts.py

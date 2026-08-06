#!/usr/bin/env bash
# Download every image in docs/audit/media-manifest.json to public/images/posts/<slug>/
# using curl (avoids Python's macOS SSL cert issue).
set -euo pipefail

MANIFEST="docs/audit/media-manifest.json"
ROOT_PUBLIC="public"

ok=0; skip=0; fail=0; total=0

# Read manifest as newline-separated "SOURCE\tLOCAL"
while IFS=$'\t' read -r source local; do
  total=$((total + 1))
  dest="${ROOT_PUBLIC}${local}"
  if [[ -s "$dest" ]]; then
    skip=$((skip + 1))
    continue
  fi
  mkdir -p "$(dirname "$dest")"
  if curl -sSL --max-time 20 -A "MujoWebsiteMigration/1.0" -o "$dest" "$source"; then
    if [[ -s "$dest" ]]; then
      ok=$((ok + 1))
    else
      rm -f "$dest"
      fail=$((fail + 1))
      echo "FAIL empty file: $local" >&2
    fi
  else
    fail=$((fail + 1))
    echo "FAIL curl: $local" >&2
  fi
done < <(python3 -c "
import json
for e in json.load(open('$MANIFEST')):
    print(f'{e[\"source\"]}\t{e[\"local\"]}')
")

echo
echo "downloaded=$ok  skipped=$skip  failed=$fail  total=$total"

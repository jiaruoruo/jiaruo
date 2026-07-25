#!/usr/bin/env python3
"""Fix raw_sha256 in wiki/sources/ frontmatter to match actual raw file hashes."""

import hashlib, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).parent.parent
WIKI_SOURCES = REPO / "wiki" / "sources"
RAW_ROOT = REPO / "raw"

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

fixed = 0
skipped = 0

for src in sorted(WIKI_SOURCES.glob("*.md")):
    text = src.read_text(encoding="utf-8")
    if not text.startswith("---"):
        skipped += 1
        continue

    # Find frontmatter boundaries
    m = re.search(r'(?m)^\-\-\-\s*$', text[3:])
    if not m:
        skipped += 1
        continue

    yaml_str = text[3:m.start() + 3]
    body = text[m.end() + 3:]

    try:
        fm = yaml.safe_load(yaml_str)
    except yaml.YAMLError:
        skipped += 1
        continue

    if not isinstance(fm, dict):
        skipped += 1
        continue

    raw_sha = fm.get("raw_sha256", "")
    raw_file = fm.get("raw_file", "")

    if not raw_sha or not raw_file:
        skipped += 1
        continue

    raw_path = REPO / raw_file
    if not raw_path.exists():
        continue

    actual = sha256_file(raw_path)
    if actual != raw_sha:
        fm["raw_sha256"] = actual
        new_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        # Ensure trailing newline after ---
        new_text = f"---\n{new_yaml}---\n{body.lstrip('\n')}"
        src.write_text(new_text, encoding="utf-8")
        print(f"  FIXED {src.relative_to(REPO)}")
        fixed += 1

print(f"\nDone: {fixed} fixed, {skipped} skipped")

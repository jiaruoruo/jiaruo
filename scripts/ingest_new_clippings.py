#!/usr/bin/env python3
"""
ingest_new_clippings.py - Batch ingest unprocessed clipping files into wiki/sources/

Usage:
    python scripts/ingest_new_clippings.py
"""

import hashlib
import re
import os
import sys
from pathlib import Path
from datetime import datetime

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# Fix stdout encoding for Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

CLIP_DIR = Path("raw/clippings")
SOURCES_DIR = Path("wiki/sources")


def slugify(name: str) -> str:
    """Convert a string to lowercase-hyphen slug."""
    name = name.lower().strip()
    # Remove characters that aren't word chars, spaces, or hyphens
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s_]+", "-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-")


def parse_clipping_frontmatter(content: str) -> dict:
    """Parse the YAML frontmatter from a clipping file."""
    if not content.startswith("---"):
        return {}
    
    match = re.search(r'(?m)^\-\-\-\s*$', content[3:])
    if not match:
        return {}
    
    yaml_content = content[3: match.start() + 3]
    try:
        fm = yaml.safe_load(yaml_content)
        if not isinstance(fm, dict):
            return {}
        return fm
    except yaml.YAMLEventError:
        return {}


def build_source_content(clip_name: str, clip_path: Path) -> str:
    """Build a wiki/source markdown file from a clipping."""
    raw_bytes = clip_path.read_bytes()
    sha256_full = hashlib.sha256(raw_bytes).hexdigest()
    
    content = clip_path.read_text(encoding="utf-8", errors="replace")
    fm = parse_clipping_frontmatter(content)
    
    # Extract metadata from clipping frontmatter
    created_str = fm.get("created", "")
    if created_str and isinstance(created_str, str):
        try:
            dt = datetime.strptime(created_str[:10], "%Y-%m-%d")
            date_str = dt.strftime("%Y-%m-%d")
        except ValueError:
            date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    source_url = fm.get("source", "")
    author = fm.get("author", "")
    
    # Extract title from first # heading (after frontmatter)
    fm_match = re.search(r'(?m)^\-\-\-\s*$', content[3:])
    if fm_match:
        body = content[fm_match.end() + 3:]
    else:
        body = content
    
    title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else clip_path.stem
    
    # Generate slug
    slug = slugify(clip_path.stem)
    
    # Determine domain from source URL
    domain = ""
    if source_url:
        domain_match = re.search(r'https?://([^/]+)', source_url)
        if domain_match:
            domain = domain_match.group(1)
    
    # Determine tags - extract from frontmatter tags or generate from title/content
    tags_list = []
    raw_tags = fm.get("tags", [])
    if isinstance(raw_tags, list) and raw_tags:
        for t in raw_tags:
            if isinstance(t, str):
                tags_list.append(t)
    
    # Always include the source page slug as a tag
    tags_list.insert(0, slug)
    
    # Format tags for YAML
    tags_yaml = "\n".join(f"  - {t}" for t in tags_list)
    
    # Build the source page content
    source_text = f"""---
type: source
title: "{title}"
date: {date_str}
source_url: "{source_url}"
domain: "{domain}"
author: "{author}"
tags:
{tags_yaml}
processed: true
raw_file: "raw/clippings/{clip_name}"
raw_sha256: "{sha256_full}"
last_verified: {date_str}
possibly_outdated: false
language: "zh"
---

# {title}

## Summary

<!-- Brief summary of the source content -->

## Key Points

- 

## Concepts Extracted

- <!-- [[concept-slug]] -->

## Entities Extracted

- <!-- [[entities/entity-slug]] -->

## Contradictions

<!-- 与其他来源的分歧，格式：
- 与 [[sources/other-source]] 在「xxx」问题上存在分歧：[具体描述] -->

## My Notes

<!-- 个人批注、延伸思考，主观内容放此处 -->
"""
    
    return source_text


def main():
    # Get already claimed raw_file basenames
    claimed = set()
    for f in SOURCES_DIR.glob("*.md"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r'raw_file:\s*(.+)', content)
        if m:
            raw = m.group(1).strip().strip('"\'')
            fname = os.path.basename(raw)
            claimed.add(fname)
    
    # Find unprocessed clippings
    unprocessed = []
    for f in sorted(CLIP_DIR.glob("*.md")):
        if f.name not in claimed:
            unprocessed.append(f)
    
    print(f"Found {len(unprocessed)} unprocessed clipping files:")
    for f in unprocessed:
        print(f"  {f.name}")
    print()
    
    # Also fix mckinsey source that has wrong raw_file date
    mckinsey_source = SOURCES_DIR / "mckinsey-humanoid-robot-bom-supply-chain.md"
    mckinsey_fixed = False
    if mckinsey_source.exists():
        src_content = mckinsey_source.read_text(encoding="utf-8")
        # Current: raw/clippings/2026-05-14... but actual file is 2026-05-20...
        if "raw/clippings/2026-05-14" in src_content:
            # Check if the actual file exists with 2026-05-20
            actual_file = CLIP_DIR / "2026-05-20麦肯锡拆解人形机器人 BOM：最贵的是执行器，最缺的是供应链.md"
            if actual_file.exists():
                actual_sha = hashlib.sha256(actual_file.read_bytes()).hexdigest()
                src_content = src_content.replace(
                    "raw/clippings/2026-05-14麦肯锡拆解人形机器人 BOM：最贵的是执行器，最缺的是供应链.md",
                    "raw/clippings/2026-05-20麦肯锡拆解人形机器人 BOM：最贵的是执行器，最缺的是供应链.md"
                )
                # Update SHA
                sha_pattern = r'(raw_sha256:\s*)"[a-f0-9]+"'
                src_content = re.sub(
                    sha_pattern,
                    lambda m: f'{m.group(1)}"{actual_sha}"',
                    src_content
                )
                mckinsey_source.write_text(src_content, encoding="utf-8")
                mckinsey_fixed = True
                print("✓ Fixed mckinsey source: updated raw_file path and SHA")
    
    # Process each unprocessed clipping
    created = 0
    skipped = 0
    for clip_path in unprocessed:
        source_content = build_source_content(clip_path.name, clip_path)
        
        # Generate source filename from slug
        slug = slugify(clip_path.stem)
        source_filename = f"{slug}.md"
        source_path = SOURCES_DIR / source_filename
        
        if source_path.exists():
            print(f"⚠ Source already exists (skipping): {source_filename}")
            skipped += 1
            continue
        
        source_path.write_text(source_content, encoding="utf-8")
        print(f"✓ Created: {source_filename}  <-  {clip_path.name}")
        created += 1
    
    print()
    print(f"=== Summary ===")
    print(f"  Created: {created} new source files")
    print(f"  Skipped: {skipped} (already exist)")
    if mckinsey_fixed:
        print(f"  Fixed: mckinsey-humanoid-robot-bom-supply-chain.md raw_file reference")
    print()


if __name__ == "__main__":
    main()
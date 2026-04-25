#!/usr/bin/env python3
"""
lint.py - Knowledge Base Health Checker
Performs 9 checks on the wiki/ directory and writes a report to wiki/outputs/lint-YYYY-MM-DD.md

Usage:
    python scripts/lint.py [--wiki-root PATH]
"""

import os
import re
import sys
import hashlib
import argparse
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

WIKI_ROOT = Path(__file__).parent.parent / "wiki"
RAW_ROOT = Path(__file__).parent.parent / "raw"
OUTPUTS_DIR = WIKI_ROOT / "outputs"

# System files excluded from most checks (they intentionally lack full frontmatter)
SYSTEM_FILES = {"index.md", "log.md", "overview.md", "QUESTIONS.md"}

# Stale thresholds by domain_volatility
STALE_DAYS = {
    "high": 90,
    "medium": 180,
    "low": 365,
}

# Jaccard similarity threshold for near-duplicate concept names
JACCARD_THRESHOLD = 0.7


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_frontmatter(filepath: Path) -> tuple[Optional[dict], str]:
    """Parse YAML frontmatter and body from a Markdown file.
    Returns (frontmatter_dict_or_None, body_text).

    Uses line-anchored regex so that '---' inside YAML values (e.g. filenames)
    does not prematurely terminate the frontmatter block.
    """
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return None, f"[READ ERROR: {e}]"

    if not text.startswith("---"):
        return None, text

    # Match closing --- only when it appears at the start of a line
    match = re.search(r'(?m)^\-\-\-\s*$', text[3:])
    if not match:
        return None, text

    yaml_content = text[3: match.start() + 3]  # +3 accounts for the skipped opening ---
    body = text[match.end() + 3:]              # skip past the closing ---

    try:
        fm = yaml.safe_load(yaml_content)
        if not isinstance(fm, dict):
            fm = None
    except yaml.YAMLError:
        fm = None

    return fm, body


def slugify(name: str) -> str:
    """Convert a string to lowercase-hyphen slug for comparison."""
    name = name.lower().strip()
    # Remove common CJK characters and punctuation for slug comparison
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s_]+", "-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-")


def jaccard_similarity(a: str, b: str) -> float:
    """Compute Jaccard similarity between two strings using character bigrams."""
    def bigrams(s):
        s = slugify(s)
        return set(s[i:i+2] for i in range(len(s) - 1)) if len(s) > 1 else set(s)

    set_a = bigrams(a)
    set_b = bigrams(b)
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)


def sha256_file(filepath: Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def collect_wiki_files(
    wiki_root: Path,
    exclude_system: bool = True,
    exclude_templates: bool = False,
    exclude_outputs: bool = False,
) -> list[Path]:
    """Collect all .md files under wiki_root, optionally excluding certain directories."""
    files = []
    for p in wiki_root.rglob("*.md"):
        if exclude_system and p.name in SYSTEM_FILES:
            continue
        if exclude_templates and "templates" in p.parts:
            continue
        if exclude_outputs and "outputs" in p.parts:
            continue
        files.append(p)
    return sorted(files)


def extract_wikilinks(text: str) -> list[str]:
    """Extract all [[target]] and [[target|alias]] wikilink targets from text.
    Skips wikilinks inside HTML comments.
    """
    # Remove HTML comments to avoid false positives from placeholder comments
    text_no_comments = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", text_no_comments)


def slug_to_path(link_target: str, wiki_root: Path) -> Optional[Path]:
    """Resolve a wikilink target to a filesystem path."""
    # Normalize: strip leading wiki/ or /
    target = link_target.strip().lstrip("/")
    if target.startswith("wiki/"):
        target = target[5:]

    # Try with and without .md extension
    candidates = [
        wiki_root / (target + ".md"),
        wiki_root / target,
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


# ---------------------------------------------------------------------------
# Check 1: YAML Frontmatter Validity
# ---------------------------------------------------------------------------

def check_frontmatter(wiki_root: Path) -> list[str]:
    """Check that all .md files have valid YAML frontmatter with 'type' and 'date'."""
    issues = []
    for filepath in collect_wiki_files(
        wiki_root, exclude_system=True, exclude_templates=True
    ):
        fm, _ = load_frontmatter(filepath)
        rel = filepath.relative_to(wiki_root.parent)

        if fm is None:
            issues.append(f"- ❌ `{rel}`: 无有效 YAML frontmatter")
            continue

        missing = []
        if "type" not in fm:
            missing.append("type")
        if "date" not in fm:
            missing.append("date")
        if missing:
            issues.append(f"- ⚠ `{rel}`: frontmatter 缺少字段：{', '.join(missing)}")

    return issues


# ---------------------------------------------------------------------------
# Check 2: Broken Wikilinks
# ---------------------------------------------------------------------------

def check_broken_wikilinks(wiki_root: Path) -> list[str]:
    """Check for [[xxx]] references to non-existent pages."""
    issues = []

    # Build set of all existing page slugs (relative to wiki root, without .md)
    existing = set()
    for p in wiki_root.rglob("*.md"):
        rel = p.relative_to(wiki_root)
        existing.add(str(rel.with_suffix("")).replace("\\", "/"))
        existing.add(p.stem)  # bare filename without path

    for filepath in collect_wiki_files(
        wiki_root, exclude_system=False, exclude_templates=True, exclude_outputs=True
    ):
        _, body = load_frontmatter(filepath)
        links = extract_wikilinks(body)
        rel = filepath.relative_to(wiki_root.parent)

        for link in links:
            target = link.strip()
            # Normalize
            target_norm = target.lstrip("/").lstrip("wiki/")
            target_bare = target_norm.split("/")[-1]

            resolved = slug_to_path(target, wiki_root)
            if resolved is None:
                # Also check bare name
                if target_norm not in existing and target_bare not in existing:
                    issues.append(f"- ❌ `{rel}`: 断链 `[[{link}]]`（目标页面不存在）")

    return issues


# ---------------------------------------------------------------------------
# Check 3: Index Consistency
# ---------------------------------------------------------------------------

def check_index_consistency(wiki_root: Path) -> list[str]:
    """Check that all files listed in wiki/index.md actually exist."""
    issues = []
    index_path = wiki_root / "index.md"

    if not index_path.exists():
        return ["- ❌ `wiki/index.md` 不存在"]

    _, body = load_frontmatter(index_path)
    links = extract_wikilinks(body)

    for link in links:
        resolved = slug_to_path(link, wiki_root)
        if resolved is None:
            issues.append(f"- ❌ `wiki/index.md` 引用了不存在的页面：`[[{link}]]`")

    return issues


# ---------------------------------------------------------------------------
# Check 4: Stub Pages
# ---------------------------------------------------------------------------

def check_stub_pages(wiki_root: Path, min_chars: int = 100) -> list[str]:
    """Check for pages with body text shorter than min_chars characters."""
    issues = []

    for filepath in collect_wiki_files(
        wiki_root, exclude_system=True, exclude_templates=True
    ):
        _, body = load_frontmatter(filepath)
        # Strip markdown headings and whitespace for content count
        content = re.sub(r"^#+\s.*$", "", body, flags=re.MULTILINE)
        content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
        content = content.strip()

        if len(content) < min_chars:
            rel = filepath.relative_to(wiki_root.parent)
            issues.append(
                f"- ⚠ `{rel}`: Stub 页面（正文约 {len(content)} 字符，少于 {min_chars}）"
            )

    return issues


# ---------------------------------------------------------------------------
# Check 5: Near-duplicate Concept Names
# ---------------------------------------------------------------------------

def check_near_duplicate_concepts(wiki_root: Path) -> list[str]:
    """Check for concept page pairs with Jaccard similarity > JACCARD_THRESHOLD."""
    issues = []
    concepts_dir = wiki_root / "concepts"

    if not concepts_dir.exists():
        return []

    concept_files = list(concepts_dir.glob("*.md"))
    names = [(p, p.stem) for p in concept_files]

    checked = set()
    for i, (path_a, name_a) in enumerate(names):
        for j, (path_b, name_b) in enumerate(names):
            if i >= j:
                continue
            pair_key = tuple(sorted([name_a, name_b]))
            if pair_key in checked:
                continue
            checked.add(pair_key)

            sim = jaccard_similarity(name_a, name_b)
            if sim > JACCARD_THRESHOLD:
                rel_a = path_a.relative_to(wiki_root.parent)
                rel_b = path_b.relative_to(wiki_root.parent)
                issues.append(
                    f"- ⚠ 近重复概念对（Jaccard={sim:.2f}）：`{rel_a}` ↔ `{rel_b}`"
                )

    return issues


# ---------------------------------------------------------------------------
# Check 6: SHA-256 Integrity
# ---------------------------------------------------------------------------

def check_sha256_integrity(wiki_root: Path, raw_root: Path) -> list[str]:
    """Compare raw file hashes against source page raw_sha256 fields."""
    issues = []
    sources_dir = wiki_root / "sources"

    if not sources_dir.exists():
        return []

    for filepath in sources_dir.glob("*.md"):
        fm, _ = load_frontmatter(filepath)
        if not fm:
            continue

        raw_sha = fm.get("raw_sha256", "")
        raw_file = fm.get("raw_file", "")

        if not raw_sha or not raw_file:
            continue

        # Resolve raw file path relative to repo root
        raw_path = raw_root.parent / raw_file
        if not raw_path.exists():
            rel = filepath.relative_to(wiki_root.parent)
            issues.append(f"- ⚠ `{rel}`: raw_file `{raw_file}` 不存在（无法验证哈希）")
            continue

        actual_sha = sha256_file(raw_path)
        if actual_sha and actual_sha != raw_sha:
            rel = filepath.relative_to(wiki_root.parent)
            issues.append(
                f"- ⚠ SOURCE MODIFIED `{rel}`: raw_sha256 不匹配\n"
                f"  - 记录值：`{raw_sha}`\n"
                f"  - 实际值：`{actual_sha}`\n"
                f"  - 文件：`{raw_file}`"
            )

    return issues


# ---------------------------------------------------------------------------
# Check 7: Stale Pages
# ---------------------------------------------------------------------------

def check_stale_pages(wiki_root: Path) -> list[str]:
    """Check pages that exceed their domain_volatility freshness threshold."""
    issues = []
    today = date.today()

    for filepath in collect_wiki_files(wiki_root, exclude_system=True):
        fm, _ = load_frontmatter(filepath)
        if not fm:
            continue

        volatility = fm.get("domain_volatility", "")
        last_reviewed = fm.get("last_reviewed", fm.get("date", None))

        if not volatility or volatility not in STALE_DAYS:
            continue
        if not last_reviewed:
            continue

        try:
            if isinstance(last_reviewed, str):
                review_date = datetime.strptime(last_reviewed, "%Y-%m-%d").date()
            elif isinstance(last_reviewed, date):
                review_date = last_reviewed
            else:
                continue
        except ValueError:
            continue

        threshold = STALE_DAYS[volatility]
        age_days = (today - review_date).days

        if age_days > threshold:
            rel = filepath.relative_to(wiki_root.parent)
            issues.append(
                f"- ⚠ Stale `{rel}`: domain_volatility={volatility}，"
                f"距上次审阅 {age_days} 天（阈值 {threshold} 天）"
            )

    return issues


# ---------------------------------------------------------------------------
# Check 8: Cross-language Duplicates
# ---------------------------------------------------------------------------

def check_cross_language_duplicates(wiki_root: Path) -> list[str]:
    """
    Detect cross-language duplicates via:
    a) Source URL similarity across source pages
    b) Overlapping aliases across different concept pages
    """
    issues = []

    # --- 8a: Source URL similarity ---
    sources_dir = wiki_root / "sources"
    if sources_dir.exists():
        url_map: dict[str, list[Path]] = {}
        for filepath in sources_dir.glob("*.md"):
            fm, _ = load_frontmatter(filepath)
            if not fm:
                continue
            url = fm.get("source_url", "").strip()
            if not url:
                continue
            # Normalize URL: strip protocol, trailing slash, www
            norm_url = re.sub(r"^https?://(www\.)?", "", url).rstrip("/").lower()
            url_map.setdefault(norm_url, []).append(filepath)

        for url, paths in url_map.items():
            if len(paths) > 1:
                rels = [str(p.relative_to(wiki_root.parent)) for p in paths]
                issues.append(
                    f"- ⚠ 跨语言重复来源（URL 相同）：{', '.join(f'`{r}`' for r in rels)}\n"
                    f"  - URL：`{url}`"
                )

    # --- 8b: Overlapping aliases across concept pages ---
    concepts_dir = wiki_root / "concepts"
    if concepts_dir.exists():
        alias_map: dict[str, list[Path]] = {}
        for filepath in concepts_dir.glob("*.md"):
            fm, _ = load_frontmatter(filepath)
            if not fm:
                continue
            aliases = fm.get("aliases", []) or []
            if isinstance(aliases, str):
                aliases = [aliases]
            for alias in aliases:
                norm = alias.strip().lower()
                alias_map.setdefault(norm, []).append(filepath)

        for alias, paths in alias_map.items():
            if len(paths) > 1:
                rels = [str(p.relative_to(wiki_root.parent)) for p in paths]
                issues.append(
                    f"- ⚠ 跨语言重复别名 `{alias}`：出现在 {', '.join(f'`{r}`' for r in rels)}"
                )

    return issues


# ---------------------------------------------------------------------------
# Check 9: Wikilink Format Compliance
# ---------------------------------------------------------------------------

def check_wikilink_format(wiki_root: Path) -> list[str]:
    """
    Check for non-lowercase-hyphen wikilinks:
    - CJK characters in wikilinks (e.g., [[价值投资]])
    - CamelCase wikilinks (e.g., [[ValueInvesting]])
    - Underscore wikilinks (e.g., [[value_investing]])
    - Alias broken links (wikilinks using display alias that differ from actual page)
    """
    issues = []
    cjk_re = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")
    camel_re = re.compile(r"[A-Z]")
    underscore_re = re.compile(r"_")

    for filepath in collect_wiki_files(wiki_root, exclude_system=False, exclude_outputs=True):
        _, body = load_frontmatter(filepath)
        # Remove HTML comments to skip placeholder examples
        body_no_comments = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
        rel = filepath.relative_to(wiki_root.parent)

        # Find all wikilinks with full syntax [[target|alias]] or [[target]]
        raw_links = re.findall(r"\[\[([^\]]+)\]\]", body_no_comments)

        for raw_link in raw_links:
            # Split target from alias
            parts = raw_link.split("|", 1)
            target = parts[0].strip()

            if cjk_re.search(target):
                issues.append(
                    f"- ❌ `{rel}`: wikilink 包含中文字符 `[[{raw_link}]]`\n"
                    f"  → 应使用英文 slug，将中文名写入 concept 页的 aliases 字段"
                )
            elif camel_re.search(target):
                issues.append(
                    f"- ⚠ `{rel}`: wikilink 使用驼峰命名 `[[{raw_link}]]`\n"
                    f"  → 应使用小写连字符格式"
                )
            elif underscore_re.search(target):
                issues.append(
                    f"- ⚠ `{rel}`: wikilink 使用下划线 `[[{raw_link}]]`\n"
                    f"  → 应使用小写连字符格式"
                )

    return issues


# ---------------------------------------------------------------------------
# Report Writer
# ---------------------------------------------------------------------------

def write_report(wiki_root: Path, results: dict[str, list[str]]) -> Path:
    """Write the lint report to wiki/outputs/lint-YYYY-MM-DD.md."""
    outputs_dir = wiki_root / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)

    today_str = date.today().strftime("%Y-%m-%d")
    report_path = outputs_dir / f"lint-{today_str}.md"

    total_issues = sum(len(v) for v in results.values())
    checks_passed = sum(1 for v in results.values() if len(v) == 0)
    checks_total = len(results)

    lines = [
        "---",
        "type: lint-report",
        f"date: {today_str}",
        "graph-excluded: true",
        "---",
        "",
        f"# Lint Report — {today_str}",
        "",
        f"**总计：{total_issues} 个问题，{checks_passed}/{checks_total} 项检查通过**",
        "",
        "---",
        "",
    ]

    check_labels = {
        "check1_frontmatter": "Check 1：YAML Frontmatter 合法性",
        "check2_broken_wikilinks": "Check 2：Broken Wikilinks",
        "check3_index_consistency": "Check 3：Index 一致性",
        "check4_stub_pages": "Check 4：Stub 页面",
        "check5_near_duplicates": "Check 5：近重复概念名称",
        "check6_sha256": "Check 6：SHA-256 完整性",
        "check7_stale": "Check 7：Stale 页面",
        "check8_cross_language": "Check 8：跨语言重复",
        "check9_wikilink_format": "Check 9：Wikilink 格式规范",
    }

    for key, label in check_labels.items():
        issues = results.get(key, [])
        status = "✅ 通过" if not issues else f"❌ {len(issues)} 个问题"
        lines.append(f"## {label} — {status}")
        lines.append("")
        if issues:
            lines.extend(issues)
        else:
            lines.append("_无问题。_")
        lines.append("")

    report_text = "\n".join(lines)
    report_path.write_text(report_text, encoding="utf-8")
    return report_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Knowledge Base Lint Checker")
    parser.add_argument(
        "--wiki-root",
        type=Path,
        default=WIKI_ROOT,
        help="Path to the wiki/ directory (default: ../wiki relative to this script)",
    )
    parser.add_argument(
        "--raw-root",
        type=Path,
        default=RAW_ROOT,
        help="Path to the raw/ directory (default: ../raw relative to this script)",
    )
    args = parser.parse_args()

    wiki_root = args.wiki_root.resolve()
    raw_root = args.raw_root.resolve()

    if not wiki_root.exists():
        print(f"ERROR: wiki root not found: {wiki_root}", file=sys.stderr)
        sys.exit(1)

    print(f"Running lint on: {wiki_root}")
    print()

    results = {}

    print("Check 1: YAML Frontmatter Validity...")
    results["check1_frontmatter"] = check_frontmatter(wiki_root)

    print("Check 2: Broken Wikilinks...")
    results["check2_broken_wikilinks"] = check_broken_wikilinks(wiki_root)

    print("Check 3: Index Consistency...")
    results["check3_index_consistency"] = check_index_consistency(wiki_root)

    print("Check 4: Stub Pages...")
    results["check4_stub_pages"] = check_stub_pages(wiki_root)

    print("Check 5: Near-duplicate Concept Names...")
    results["check5_near_duplicates"] = check_near_duplicate_concepts(wiki_root)

    print("Check 6: SHA-256 Integrity...")
    results["check6_sha256"] = check_sha256_integrity(wiki_root, raw_root)

    print("Check 7: Stale Pages...")
    results["check7_stale"] = check_stale_pages(wiki_root)

    print("Check 8: Cross-language Duplicates...")
    results["check8_cross_language"] = check_cross_language_duplicates(wiki_root)

    print("Check 9: Wikilink Format Compliance...")
    results["check9_wikilink_format"] = check_wikilink_format(wiki_root)

    print()
    report_path = write_report(wiki_root, results)
    print(f"Report written to: {report_path}")
    print()

    # Summary to stdout
    total = sum(len(v) for v in results.values())
    passed = sum(1 for v in results.values() if not v)
    print(f"=== Summary: {passed}/{len(results)} checks passed, {total} issues found ===")

    for key, issues in results.items():
        label = key.replace("_", " ").title()
        status = "PASS" if not issues else f"FAIL ({len(issues)} issues)"
        print(f"  {label}: {status}")

    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

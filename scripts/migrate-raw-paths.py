#!/usr/bin/env python3
"""
migrate-raw-paths.py - 批量迁移 wiki/sources 的 raw_file 路径

背景：raw/ 目录从扁平结构迁移到 raw/工作/{type}/{topic}/ 三级结构。
本脚本：
  1. 扫描 raw/工作/ 下所有文件，建立「文件名 → 新路径」映射
  2. 遍历所有 wiki/sources/*.md，找出 raw_file 字段
  3. 如果旧路径文件不存在但同名文件在新位置找到了，则更新路径并重新计算 SHA-256
  4. 输出迁移报告

用法：
    python scripts/migrate-raw-paths.py [--dry-run]
"""

import os
import re
import sys
import hashlib
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
WIKI_SOURCES = REPO_ROOT / "wiki" / "sources"
RAW_ROOT = REPO_ROOT / "raw"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_new_path_index() -> dict[str, list[Path]]:
    """扫描 raw/ 下所有文件，建立文件名 -> [路径列表] 映射"""
    index: dict[str, list[Path]] = {}
    for root, dirs, files in os.walk(RAW_ROOT):
        for fname in files:
            full = Path(root) / fname
            key = fname
            if key not in index:
                index[key] = []
            index[key].append(full)
    return index


def parse_frontmatter(content: str):
    """返回 (frontmatter_dict, frontmatter_raw_str, body_after_yaml)"""
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", content, re.DOTALL)
    if not match:
        return None, None, content
    try:
        fm = yaml.safe_load(match.group(1))
        return fm, match.group(1), match.group(2)
    except Exception:
        return None, None, content


def update_frontmatter_field(content: str, field: str, new_value: str) -> str:
    """替换 frontmatter 中特定字段的值（保留原有缩进和格式）"""
    pattern = rf"^({re.escape(field)}:\s*)(.+)$"
    replacement = rf"\g<1>{new_value}"
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if count == 0:
        # 字段不存在，插入到 frontmatter 末尾
        new_content = content.replace("\n---\n", f"\n{field}: {new_value}\n---\n", 1)
    return new_content


def main():
    parser = argparse.ArgumentParser(description="Migrate raw_file paths after raw/ restructuring")
    parser.add_argument("--dry-run", action="store_true", help="只分析，不修改文件")
    args = parser.parse_args()

    dry_run = args.dry_run
    if dry_run:
        print("=== DRY RUN 模式：不修改任何文件 ===\n")

    # 1. 建立新路径索引
    print("扫描新 raw/ 目录结构...")
    new_index = build_new_path_index()
    total_new_files = sum(len(v) for v in new_index.values())
    print(f"  找到 {total_new_files} 个文件，{len(new_index)} 个不同文件名\n")

    # 2. 遍历 wiki/sources
    source_files = sorted(WIKI_SOURCES.glob("*.md"))
    print(f"扫描 wiki/sources/*.md：{len(source_files)} 个文件\n")

    stats = {
        "updated": 0,
        "already_ok": 0,
        "not_found_old_path_only": 0,   # 旧路径不存在，新路径也找不到（真正找不到）
        "ambiguous": 0,                  # 多个新路径匹配同一文件名
        "no_raw_file": 0,
        "skipped_redirect": 0,
    }

    updated_list = []
    not_found_list = []
    ambiguous_list = []

    for src_path in source_files:
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        fm, fm_raw, body = parse_frontmatter(content)
        if fm is None:
            continue

        # 跳过 redirect 文件
        if fm.get("type") == "redirect":
            stats["skipped_redirect"] += 1
            continue

        raw_file = fm.get("raw_file", "")
        if not raw_file:
            stats["no_raw_file"] += 1
            continue

        raw_file_path = REPO_ROOT / raw_file

        # 如果当前路径已经有效，跳过
        if raw_file_path.exists():
            stats["already_ok"] += 1
            continue

        # 旧路径失效，查找同名文件
        fname = Path(raw_file).name
        candidates = new_index.get(fname, [])

        if len(candidates) == 0:
            stats["not_found_old_path_only"] += 1
            not_found_list.append((src_path.name, raw_file))
            continue

        if len(candidates) > 1:
            # 尝试用原路径的类型目录（articles/clippings/pdfs/notes/personal/images）消歧
            orig_parts = Path(raw_file).parts  # e.g. ('raw', 'articles', 'xxx.md')
            type_dir = orig_parts[1] if len(orig_parts) >= 2 else ""
            refined = [c for c in candidates if type_dir in c.parts]
            if len(refined) == 1:
                candidates = refined
            else:
                stats["ambiguous"] += 1
                ambiguous_list.append((src_path.name, raw_file, [str(c.relative_to(REPO_ROOT)) for c in candidates]))
                continue

        # 唯一匹配
        new_path = candidates[0]
        new_raw_file = str(new_path.relative_to(REPO_ROOT)).replace("\\", "/")
        new_sha256 = sha256_file(new_path)

        updated_list.append((src_path.name, raw_file, new_raw_file))
        stats["updated"] += 1

        if not dry_run:
            # 更新文件内容
            new_content = update_frontmatter_field(content, "raw_file", new_raw_file)
            new_content = update_frontmatter_field(new_content, "raw_sha256", new_sha256)
            with open(src_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(new_content)

    # 3. 输出报告
    print("=" * 60)
    print("迁移报告")
    print("=" * 60)
    print(f"  [OK]  已更新路径：      {stats['updated']} 个")
    print(f"  [OK]  路径已正确：      {stats['already_ok']} 个")
    print(f"  [--]  无 raw_file：     {stats['no_raw_file']} 个")
    print(f"  [!!]  路径模糊（多匹配）：{stats['ambiguous']} 个")
    print(f"  [XX]  找不到对应文件：  {stats['not_found_old_path_only']} 个")
    print(f"  [>>]  redirect 跳过：   {stats['skipped_redirect']} 个")
    print()

    if ambiguous_list:
        print("[!!] 需要人工处理（多个候选）：")
        for src, old, candidates in ambiguous_list:
            print(f"  {src}:")
            print(f"    旧: {old}")
            for c in candidates:
                print(f"    新候选: {c}")
        print()

    if not_found_list:
        print("[XX] 找不到对应文件（需人工处理）：")
        for src, old in not_found_list:
            print(f"  {src}: {old}")
        print()

    if dry_run:
        print("（DRY RUN：以上为预览，未修改任何文件）")
        if updated_list:
            print("\n将要更新的前10条：")
            for src, old, new in updated_list[:10]:
                print(f"  {src}")
                print(f"    旧: {old}")
                print(f"    新: {new}")
    else:
        print(f"[DONE] 迁移完成，共更新 {stats['updated']} 个文件")

    return 0 if stats["not_found_old_path_only"] == 0 and stats["ambiguous"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

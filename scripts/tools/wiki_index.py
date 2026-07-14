#!/usr/bin/env python3
"""wiki_index.py — 轻量关键词检索引擎（qmd 缺席时的程序化 fallback）

背景：CLAUDE.md 原依赖外部语义检索引擎 `qmd`（带嵌入向量），但该工具
本仓库不分发、且当前维护环境未安装。为避免「qmd 报错 → 纯人工扫 index.md」
的不可复现路径，本脚本提供纯 stdlib + PyYAML 的关键词级检索/扫描/统计，
覆盖 qmd 的 query / multi-get / status / update / add / embed 子命令形态。

不支持语义嵌入（embed 需 qmd）。检索为 frontmatter(title/aliases/tags)
+ 正文关键词命中排名，足够本库规模的降级需求。

用法：
  python scripts/tools/wiki_index.py query "文本" [--json] [--top N]
  python scripts/tools/wiki_index.py multi-get "wiki/concepts/*.md" [--lines N]
  python scripts/tools/wiki_index.py status
  python scripts/tools/wiki_index.py update        # fallback: no-op
  python scripts/tools/wiki_index.py add           # fallback: no-op
  python scripts/tools/wiki_index.py embed         # 提示需 qmd
"""
import os
import re
import sys
import json
import glob
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

REPO = Path(__file__).resolve().parent.parent.parent  # scripts/tools -> repo root
WIKI = REPO / "wiki"

# 这些目录/类型在「知识检索」时应排除（过程产物与系统文件）
GRAPH_EXCLUDED_DIRS = {"outputs"}
GRAPH_EXCLUDED_TYPES = {"system-index", "system-overview", "system-log", "output"}


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    fm = {}
    if yaml:
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception:
            fm = {}
    return (fm if isinstance(fm, dict) else {}), body


def iter_wiki_pages(exclude_graph_excluded=True):
    for p in WIKI.rglob("*.md"):
        rel = p.relative_to(REPO).as_posix()
        if "templates/" in rel:
            continue  # 模板不是知识实例，不计入统计/检索
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        if exclude_graph_excluded:
            if fm.get("graph-excluded") or fm.get("type") in GRAPH_EXCLUDED_TYPES:
                continue
            if any(rel.startswith(d + "/") for d in GRAPH_EXCLUDED_DIRS):
                continue
        yield rel, fm, body


def _as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _first_snippet(body):
    for line in body.splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            return s[:120]
    return ""


def cmd_query(args):
    q = args.text.strip()
    terms = [t for t in re.split(r"\s+", q) if t]
    candidates = []
    for rel, fm, body in iter_wiki_pages():
        title = str(fm.get("title", ""))
        aliases = [str(a) for a in _as_list(fm.get("aliases"))]
        tags = [str(t) for t in _as_list(fm.get("tags"))]
        hay = {
            "title": title,
            "aliases": " ".join(aliases),
            "tags": " ".join(tags),
            "body": body,
        }
        weights = {"title": 5, "aliases": 4, "tags": 3, "body": 1}
        score = 0
        search_terms = terms if terms else [q]
        for term in search_terms:
            for key, w in weights.items():
                score += hay[key].count(term) * w
        if score > 0:
            candidates.append(
                {"path": rel, "score": score, "snippet": _first_snippet(body)}
            )
    candidates.sort(key=lambda x: (-x["score"], x["path"]))
    top = candidates[: args.top]
    if args.json:
        print(json.dumps(top, ensure_ascii=False, indent=2))
    else:
        if not top:
            print("No results (fallback keyword search).")
        for c in top:
            print(f"{c['score']:>4}  {c['path']}")
            if c["snippet"]:
                print(f"       {c['snippet']}")


def cmd_multi_get(args):
    files = sorted(glob.glob(str(REPO / args.glob)))
    if not files:
        print(f"[wiki_index] no files matched: {args.glob}")
        return
    for f in files:
        p = Path(f)
        text = p.read_text(encoding="utf-8", errors="ignore")
        print(f"===== {p.relative_to(REPO).as_posix()} =====")
        for i, line in enumerate(text.splitlines()):
            if i >= args.lines:
                break
            print(line)


def cmd_status(args):
    counts = {}
    for rel, fm, body in iter_wiki_pages(exclude_graph_excluded=False):
        t = fm.get("type", "unknown")
        counts[t] = counts.get(t, 0) + 1
    for t in sorted(counts):
        print(f"{t:20} {counts[t]}")
    print(f"{'TOTAL':20} {sum(counts.values())}")


def cmd_update(args):
    print("[wiki_index] fallback 模式：无需索引更新（qmd 专属）。文件树即为实时索引。")


def cmd_add(args):
    print("[wiki_index] fallback 模式：无需 add（qmd 专属）。")


def cmd_embed(args):
    print("[wiki_index] 语义嵌入需 qmd（带向量引擎）；fallback 为关键词检索，embed 不支持。")


def main():
    ap = argparse.ArgumentParser(description="wiki keyword index (qmd fallback)")
    sub = ap.add_subparsers(dest="cmd")
    q = sub.add_parser("query")
    q.add_argument("text")
    q.add_argument("--json", action="store_true")
    q.add_argument("--top", type=int, default=5)
    mg = sub.add_parser("multi-get")
    mg.add_argument("glob")
    mg.add_argument("--lines", type=int, default=40)
    sub.add_parser("status")
    sub.add_parser("update")
    sub.add_parser("add")
    sub.add_parser("embed")
    args = ap.parse_args()
    if args.cmd == "query":
        cmd_query(args)
    elif args.cmd == "multi-get":
        cmd_multi_get(args)
    elif args.cmd == "status":
        cmd_status(args)
    elif args.cmd == "update":
        cmd_update(args)
    elif args.cmd == "add":
        cmd_add(args)
    elif args.cmd == "embed":
        cmd_embed(args)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()

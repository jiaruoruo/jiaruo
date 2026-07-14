#!/usr/bin/env python3
"""build_domains.py — 生成 wiki/domains.md 领域导航页

按主题域受控词表（embodied-ai / automotive-eea / chip / edge-ai / agent /
finance）扫描 wiki/{concepts,entities,synthesis} 的 `tags` 字段，归类生成
导航页。一个页面可同时属于多个域；无主域标签的页面列入「待归类」，
用于暴露 P1-1（tags 受控词表）推行前的历史缺口。

用法：
  python scripts/tools/build_domains.py
"""
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

REPO = Path(__file__).resolve().parent.parent.parent
WIKI = REPO / "wiki"

DOMAINS = {
    "embodied-ai": "具身智能 / 人形机器人",
    "automotive-eea": "汽车 EEA / MCU-less / 车载通信",
    "chip": "芯片设计 / 制造 / 封装",
    "edge-ai": "端侧推理 / TinyML",
    "agent": "Agent 架构 / MCP / 治理",
    "finance": "金融数据 / 量化",
}


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


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def main():
    buckets = {d: [] for d in DOMAINS}
    untagged = []
    for sub in ("concepts", "entities", "synthesis"):
        d = WIKI / sub
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            text = p.read_text(encoding="utf-8", errors="ignore")
            fm, _ = parse_frontmatter(text)
            tags = [str(t) for t in as_list(fm.get("tags"))]
            title = str(fm.get("title", p.stem))
            link = f"[[{sub}/{p.stem}]]"
            matched = [dom for dom in DOMAINS if dom in tags]
            if not matched:
                untagged.append(f"- {link}（{title}）— tags: {tags or '无'}")
                continue
            for dom in matched:
                buckets[dom].append(f"- {link}（{title}）")

    lines = [
        "---",
        "type: system-domains",
        "graph-excluded: true",
        "---",
        "",
        "# 知识库领域导航（Domains）",
        "",
        "> 由 `scripts/tools/build_domains.py` 自动生成，按主题域受控词表归类。",
        "> 一个页面可同时属于多个域。无主域标签的页面见文末「待归类」。",
        "> 主域标签定义见 CLAUDE.md「主题域标签（tags）受控词表」。",
        "",
    ]
    for dom, desc in DOMAINS.items():
        lines.append(f"## {desc}（`{dom}`）")
        lines.append("")
        if buckets[dom]:
            lines.extend(buckets[dom])
        else:
            lines.append("_（暂无）_")
        lines.append("")

    lines.append("## 待归类（无主域标签）")
    lines.append("")
    if untagged:
        lines.extend(untagged)
    else:
        lines.append("_（无）_")
    lines.append("")

    out = WIKI / "domains.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"[build_domains] wrote {out}")
    print(
        f"  已归类: {sum(len(v) for v in buckets.values())} 页；"
        f"待归类: {len(untagged)} 页"
    )


if __name__ == "__main__":
    main()

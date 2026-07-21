#!/usr/bin/env python3
"""临时脚本：索引新增的 wiki source 文件"""
import os, re, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

new_sources = [
    'wiki/sources/cost-analysis-public-v0-4.md',
    'wiki/sources/ethercat-gpan-validation-design-2026-04.md',
    'wiki/sources/ethercat-igh-master-plan.md',
    'wiki/sources/ethercat-industry-report-2025.md',
    'wiki/sources/ethercat-team-planning-report-2026.md',
    'wiki/sources/gpan-application-scenario-vsdx.md',
    'wiki/sources/gpan-ethercat-replacement-feasibility.md',
    'wiki/sources/gpan-function-clarification-v4-1.md',
    'wiki/sources/gpan-mculess-application-analysis-v0-8.md',
    'wiki/sources/gpan-mculess-distributed-audio-v1-8.md',
    'wiki/sources/gpan-mculess-validation-report.md',
    'wiki/sources/gpan-spec-introduction-v0-2.md',
    'wiki/sources/gpan-vs-ethercat-architecture-comparison.md',
    'wiki/sources/humanoid-robot-oem-supplier-opportunities.md',
    'wiki/sources/llm-benchmark-comparison-2026-04.md',
    'wiki/sources/mcu-less-application-opportunities.md',
    'wiki/sources/mcu-less-auto-robot-insight.md',
    'wiki/sources/mcu-less-seats-project-2026-03.md',
    'wiki/sources/mcu-less-technology-insight-core.md',
    'wiki/sources/mcu-less-technology-overview.md',
    'wiki/sources/mculess-technology-insight-full-2026-05.md',
    'wiki/sources/packet-analysis-ethercat-gpan.md',
    'wiki/sources/windows-soem-ethercat-master.md',
]

new_other = [
    'wiki/domains.md',
    'wiki/outputs/2026-07-14-architecture-audit.md',
    'wiki/outputs/2026-07-14-dexterous-hand-technical-route-analysis.md',
    'wiki/outputs/lint-2026-07-14.md',
]

for fp in new_sources + new_other:
    try:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        base = os.path.basename(fp)
        title = os.path.splitext(base)[0]
        source_ref = ''
        desc = ''
        tags_list = []
        if m:
            fm_text = m.group(1)
            body = content[m.end():]
            for line in fm_text.split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    k = k.strip()
                    v = v.strip()
                    if k == 'title':
                        title = v
                    elif k == 'source':
                        source_ref = v
                    elif k == 'description':
                        desc = v[:120]
                    elif k == 'tags':
                        # handle tags: [a, b, c] or tags: a, b, c
                        v = v.strip('[]')
                        tags_list = [t.strip() for t in v.split(',') if t.strip()]
            for line in body.split('\n'):
                s = line.strip()
                if s and not s.startswith('#') and not s.startswith('---') and len(s) > 20:
                    desc = desc or s[:150]
                    break
        tags_str = ', '.join(tags_list) if tags_list else ''
        cat = 'source' if '/sources/' in fp else ('output' if '/outputs/' in fp else 'other')
        print(f'[{cat:>6s}] {title}')
        if tags_str:
            print(f'         tags: {tags_str}')
        if desc:
            print(f'         {desc[:200]}')
        print()
    except Exception as e:
        print(f'[ERROR] {fp}: {e}')

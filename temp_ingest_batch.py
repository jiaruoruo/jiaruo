#!/usr/bin/env python3
"""临时脚本：为新增 raw/clippings 计算 SHA-256 + 提取基本信息"""
import os, re, sys, hashlib

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

files = [
    'raw/clippings/2026-07-14-AI Agent评测体系：四层质量评估框架.md',
    'raw/clippings/2026-07-14-不用改模型，只调Harness！让Agent便宜又好用.md',
    'raw/clippings/2026-07-16-万字复盘：从模型到可用Agent，WorkBuddy的Harness工程是怎么做的？.md',
]

for fp in files:
    if not os.path.exists(fp):
        print(f'SKIP (not found): {fp}')
        continue
    h = hashlib.sha256()
    with open(fp, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    sha = h.hexdigest()
    
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # extract frontmatter
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    title = os.path.basename(fp).replace('.md', '')
    source_url = ''
    author = ''
    created = ''
    if m:
        fm = m.group(1)
        for line in fm.split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                k = k.strip()
                v = v.strip()
                if k == 'source':
                    source_url = v
                elif k == 'author':
                    author = v
                elif k == 'created':
                    created = v[:10]
    
    # count lines
    nlines = len(content.split('\n'))
    
    print(f'=== {title} ===')
    print(f'  sha256: {sha}')
    print(f'  source: {source_url}')
    print(f'  author: {author}')
    print(f'  date: {created}')
    print(f'  lines: {nlines}')
    
    # slug
    # simple slug: remove non-alphanumeric, lowercase
    slug_candidates = {
        'AI Agent评测体系：四层质量评估框架': 'ai-agent-evaluation-framework-four-layers',
        '不用改模型，只调Harness！让Agent便宜又好用': 'langchain-harness-tuning-nemotron-playbook',
        '万字复盘：从模型到可用Agent，WorkBuddy的Harness工程是怎么做的？': 'workbuddy-harness-engineering-case-study',
    }
    for k, v in slug_candidates.items():
        if k in title:
            print(f'  slug: {v}')
            break
    print()

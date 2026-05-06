"""
修复 wiki/sources/ 下缺少 raw_file 和 raw_sha256 字段的 source 文件。
同时更新 scripts/sha_clippings.txt。
"""
import re, os

SOURCES_DIR = r'd:\AI\LLM-WIKI\jiaruo\wiki\sources'
SHA_CLIPPINGS = r'd:\AI\LLM-WIKI\jiaruo\scripts\sha_clippings.txt'

# 映射: source文件名 → (clipping文件名, 完整SHA256, ingest日期, SHA已变更标记)
FIXES = {
    'scalar-vector-tensor-concepts.md': {
        'clip': '2026-04-25标量、矢量(向量)、张量（tensors）的理解.md',
        'sha': '4d21f655708af7456075c654064b473a7061fc302cbf4e0e5255dceffe5ee0b1',
        'date': '2026-04-25',
        'sha_changed': False,
    },
    'mculess-vendor-research-report.md': {
        'clip': 'MCULess调研报告.md',
        'sha': '270332ab2338f56597765016a28a064d2082e2bb5be9a6f86239aa363e43ea9e',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'mculess-eea-implementation-deep-dive.md': {
        'clip': '2026-04-28MCU-less架构在汽车电子中的实现路径深度解析.md',
        'sha': 'dd1ba0a074fc3dbc5efda374e560be7db8f3aca323625d0d743241e9aa417c02',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'zcu-mculess-next-gen-architecture.md': {
        'clip': '2026-04-28下一代汽车电子架构革命：MCU Less技术如何重塑区域控制器设计？.md',
        'sha': 'fb0822785a21530964f99f95de033a9ba18714576cd55af309f23d3397e97771',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'mculess-edge-node-tech-evolution.md': {
        'clip': '2026-04-28从分布式ECU到MCU-less边缘节点的技术演进之路.md',
        'sha': 'e396099781d6268f1de134012c4a8279e9bf333af6430d4e05839293d3396f65',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'mculess-ecu-central-computing-path.md': {
        'clip': '2026-04-28汽车ECU的MCU-less变革：从分布式走向中央计算的关键路径.md',
        'sha': 'b6697bab71dbc79b3d6423070b23dc64b01eea802a62c60ea2de1d0f18a956a8',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'mculess-hardware-simplification-revolution.md': {
        'clip': '2026-04-28硬件极简化革命：从传统ECU到MCU-less边缘节点的设计变革.md',
        'sha': '9c17ce58b5025a803b7664db45ed5bd418acf81904a13440941596930e69d5d0',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'mculess-10baset1s-rcp-discussion.md': {
        'clip': '2026-04-28聊一聊MCULess, 10BASE-T1S以及RCP.md',
        'sha': '304dbdfacbcac22ffa42cb45ac2c28b8a2fc9f7119b2c2d855f79697e2faba6a',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'mculess-smart-lighting-innovation.md': {
        'clip': '2026-04-28车灯技术迎来新变革？MCU-Less方案正在重新定义智能车灯.md',
        'sha': '3c48e27b7757969f3b5009622eab21b2525d3cc247017807dabb9d5585581765',
        'date': '2026-04-28',
        'sha_changed': True,  # 原始 sha256: f28dd641，文件已被修改
    },
    'zcu-market-research-2025.md': {
        'clip': '2026-04-28车身(区域)研究：ZCU搭载量超200万辆，向\u201c即插即用\u201d模块化平台演进.md',
        'sha': '8bb89b94b6e00309650f11ad9d27f6a4eb9b2a7268e38718980433f35a0e86db',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'sdv-architecture-revolution.md': {
        'clip': '2026-04-28软件定义汽车的背后：一场架构的\u201c深层次革命\u201d.md',
        'sha': '1405e3c95e520625badc2b6f7380d2ebc1c23b2dce58dfa803e9a2ae4814a529',
        'date': '2026-04-28',
        'sha_changed': False,
    },
    'beijing-auto-show-2026-eea-analysis.md': {
        'clip': '2026-05-022026北京车展新能源汽车电子电器架构总结、技术对标及应用解析.md',
        'sha': '46b38b144990aafe1bed67fa76ab062ffe171db0fcae4abaa777e4a510ff2e2f',
        'date': '2026-05-04',
        'sha_changed': False,
    },
    'tesla-optimus-dexterous-hand-patents-2026.md': {
        'clip': '2026-05-02特斯拉公开五份灵巧手专利，\u201c最难部分\u201d难在哪里？.md',
        'sha': '4f28febffaf5cb32769688eaf9cf86a8722e92af7a7a0e984ce3225595cfd501',
        'date': '2026-05-02',
        'sha_changed': False,
    },
    'honor-robot-china-suppliers-2026.md': {
        'clip': '2026-05-02荣耀机器人背后，7家中国供应商！.md',
        'sha': 'c5ea4b334ca0a322c21bb18ddab59e3f7e9cc2b9c3aa9552a907e701234f4c85',
        'date': '2026-05-02',
        'sha_changed': False,
    },
    '10baset1s-deep-dive-automotive-architecture-revolution.md': {
        'clip': '2026-05-0510BASE-T1S技术深度解析与汽车电子架构革命.md',
        'sha': '5a296f8a42ebd8d603b226d372cb6ae8e5bad45518752d8e37f4425ad24bca7a',
        'date': '2026-05-05',
        'sha_changed': False,
    },
    '10baset1s-automotive-ethernet-technical-analysis.md': {
        'clip': '2026-05-0510BASE-T1S汽车以太网技术深度解析.md',
        'sha': 'b5f581a8b8c7cb567ae708123c2a1d67b47bf02a356b70f8fbd02ac270e047e7',
        'date': '2026-05-05',
        'sha_changed': False,
    },
    'podl-automotive-ethernet-power-delivery.md': {
        'clip': '2026-05-05PoDL技术在汽车以太网供电的创新应用.md',
        'sha': '315c51247b54159c466ffc011ef95d497992c24d9019bc4f5c1bc5de7b854893',
        'date': '2026-05-05',
        'sha_changed': False,
    },
    'rcp-protocol-mculess-hardware-control-deep-dive.md': {
        'clip': '2026-05-05RCP协议深度解析：MCU-less架构下如何实现远程硬件控制.md',
        'sha': 'b796da158e61eec6783769c12209a56cad3fb2c7c723c8a0fae486fc2c0f3737',
        'date': '2026-05-05',
        'sha_changed': False,
    },
    'rcp-protocol-automotive-architecture-paradigm-shift.md': {
        'clip': '2026-05-05RCP远程控制协议的革命性创新：汽车电子架构的范式转移.md',
        'sha': 'a9c67f2c911ad87035e05563563bd8a5c617e4d1033ab787f794ae047190e038',
        'date': '2026-05-05',
        'sha_changed': False,
    },
    'automotive-ethernet-evolution-10baset1s-to-1gbase.md': {
        'clip': '2026-05-05汽车以太网技术深度解析：从10BASE-T1S到1000BASE-T1的全面演进.md',
        'sha': 'd4ae84be41a9d71a37e7ad70c205e83da20219f89c3457186cf97543f31cb3d4',
        'date': '2026-05-05',
        'sha_changed': False,
    },
    'sdv-rce-edge-node-zone-architecture.md': {
        'clip': '2026-05-05软件定义汽车时代：RCE边缘节点与区域架构的深度变革.md',
        'sha': '8eb32df64aa9c9c6942e2f355ed613c5da0961b61475497a81647f466f9dfdb4',
        'date': '2026-05-05',
        'sha_changed': False,
    },
}

def fix_file(fpath, clip_file, sha, date, sha_changed):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 解析frontmatter
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL)
    if not m:
        print(f'  ERROR: 无frontmatter: {os.path.basename(fpath)}')
        return False

    fm = m.group(1)
    body = m.group(2)

    changed = False

    # 1. 确保 type: source
    if not re.search(r'^type:', fm, re.MULTILINE):
        fm = 'type: source\n' + fm
        changed = True

    # 2. 修复 raw: → raw_file:（对 scalar 和 vendor-report）
    if re.search(r'^raw:\s', fm, re.MULTILINE):
        fm = re.sub(r'^raw:\s', 'raw_file: ', fm, flags=re.MULTILINE)
        changed = True

    # 3. 处理旧式 sha256: <abbreviated> → 替换为完整 raw_sha256 + 添加 raw_file
    if re.search(r'^sha256:', fm, re.MULTILINE):
        fm = re.sub(
            r'^sha256:\s*\S+',
            f'raw_sha256: {sha}\nraw_file: "raw/clippings/{clip_file}"',
            fm, flags=re.MULTILINE
        )
        changed = True

    # 4. 修复已有的缩写 raw_sha256 → 完整值
    existing_sha = re.search(r'^raw_sha256:\s*(\S+)', fm, re.MULTILINE)
    if existing_sha and len(existing_sha.group(1)) < 64:
        fm = re.sub(r'^raw_sha256:\s*\S+', f'raw_sha256: {sha}', fm, flags=re.MULTILINE)
        changed = True

    # 5. 添加 raw_file（如果还没有）
    if not re.search(r'^raw_file:', fm, re.MULTILINE):
        if not fm.endswith('\n'):
            fm += '\n'
        fm += f'raw_file: "raw/clippings/{clip_file}"\n'
        changed = True

    # 6. 添加 raw_sha256（如果还没有）
    if not re.search(r'^raw_sha256:', fm, re.MULTILINE):
        if not fm.endswith('\n'):
            fm += '\n'
        fm += f'raw_sha256: {sha}\n'
        changed = True

    # 7. 添加 last_verified（如果还没有）
    if not re.search(r'^last_verified:', fm, re.MULTILINE):
        if not fm.endswith('\n'):
            fm += '\n'
        fm += f'last_verified: {date}\n'
        changed = True

    # 8. 如果 SHA 已变更，添加变更注记
    if sha_changed and 'possibly_outdated' not in fm:
        if not fm.endswith('\n'):
            fm += '\n'
        fm += f'# ⚠ raw source modified: sha changed from f28dd641 to {sha[:8]}\n'
        changed = True

    if not changed:
        print(f'  SKIP (no changes needed): {os.path.basename(fpath)}')
        return False

    new_content = f'---\n{fm}---\n{body}'
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  FIXED: {os.path.basename(fpath)}')
    return True

# 读取现有 sha_clippings.txt
with open(SHA_CLIPPINGS, 'r', encoding='utf-8') as f:
    existing_sha_lines = f.read().strip()
existing_entries = {}
for line in existing_sha_lines.splitlines():
    parts = line.strip().split(' ', 1)
    if len(parts) == 2:
        existing_entries[parts[1]] = parts[0]

# 从 all_shas.txt 读取完整的 SHA 数据
ALL_SHAS_FILE = r'd:\AI\LLM-WIKI\jiaruo\scripts\all_shas.txt'
all_shas = {}
with open(ALL_SHAS_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('  ', 1)
        if len(parts) == 2:
            all_shas[parts[1]] = parts[0]

print('=== 修复 source 文件 frontmatter ===')
fixed_count = 0
for src_fname, info in FIXES.items():
    fpath = os.path.join(SOURCES_DIR, src_fname)
    if not os.path.exists(fpath):
        print(f'  NOT FOUND: {src_fname}')
        continue
    ok = fix_file(fpath, info['clip'], info['sha'], info['date'], info['sha_changed'])
    if ok:
        fixed_count += 1

print(f'\n共修复 {fixed_count} 个文件')

# 更新 sha_clippings.txt（追加新文件）
print('\n=== 更新 sha_clippings.txt ===')
new_entries = []
for fname, sha in all_shas.items():
    short = sha[:8]
    if fname not in existing_entries:
        new_entries.append(f'{short} {fname}')
        print(f'  NEW: {short} {fname}')

if new_entries:
    with open(SHA_CLIPPINGS, 'a', encoding='utf-8') as f:
        f.write('\n')
        for entry in new_entries:
            f.write(entry + '\n')
    print(f'追加了 {len(new_entries)} 个新条目到 sha_clippings.txt')
else:
    print('sha_clippings.txt 已是最新')

# 更新被修改文件的 SHA
if 'mculess-smart-lighting-innovation' in ''.join(existing_entries):
    # 更新 f28dd641 → 3c48e27b
    new_content = existing_sha_lines.replace(
        'f28dd641 2026-04-28车灯技术迎来新变革？MCU-Less方案正在重新定义智能车灯.md',
        '3c48e27b 2026-04-28车灯技术迎来新变革？MCU-Less方案正在重新定义智能车灯.md'
    )
    # Also add new files
    for entry in new_entries:
        new_content += '\n' + entry
    with open(SHA_CLIPPINGS, 'w', encoding='utf-8') as f:
        f.write(new_content + '\n')
    print('已更新车灯文件的 SHA（f28dd641 → 3c48e27b）')

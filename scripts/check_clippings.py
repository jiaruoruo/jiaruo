import hashlib, os, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

clip_dir = r'd:\AI\LLM-WIKI\jiaruo\raw\clippings'
sources_dir = r'd:\AI\LLM-WIKI\jiaruo\wiki\sources'

# 计算所有clipping文件的SHA256
clip_shas = {}
for fname in sorted(os.listdir(clip_dir)):
    if fname.endswith('.md'):
        fpath = os.path.join(clip_dir, fname)
        sha = sha256_file(fpath)
        clip_shas[fname] = sha

# 读取所有wiki/sources/*.md中的raw_sha256字段和raw_file字段
source_data = {}
for fpath in glob.glob(os.path.join(sources_dir, '*.md')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read(600)
    m_sha = re.search(r'raw_sha256:\s*([a-f0-9]+)', content)
    m_file = re.search(r'raw_file:\s*(.+)', content)
    if m_sha:
        source_data[os.path.basename(fpath)] = {
            'sha': m_sha.group(1),
            'raw_file': m_file.group(1).strip() if m_file else ''
        }

all_source_shas = {v['sha'] for v in source_data.values()}

# 找出clippings中没有对应source SHA的文件
print(f'Clipping文件总数: {len(clip_shas)}')
print(f'Sources文件总数（含sha）: {len(source_data)}')
print()

unprocessed = []
for fname, sha in sorted(clip_shas.items()):
    if sha not in all_source_shas:
        unprocessed.append((fname, sha[:16]))

print(f'未找到对应source SHA的clippings: {len(unprocessed)}')
for fname, sha in unprocessed:
    print(f'  {sha}  {fname}')

print()
print('=== 已处理对应关系 (clipping -> source) ===')
for src_fname, data in sorted(source_data.items()):
    raw_file = data['raw_file']
    if 'clippings' in raw_file:
        print(f'  {src_fname}  <-  {os.path.basename(raw_file)}')

import os, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

sources_dir = r'd:\AI\LLM-WIKI\jiaruo\wiki\sources'
clip_dir = r'd:\AI\LLM-WIKI\jiaruo\raw\clippings'

# 读取所有source文件中的raw_file字段
claimed_raw_files = set()
sources_without_rawfile = []
for fpath in glob.glob(os.path.join(sources_dir, '*.md')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read(800)
    m = re.search(r'raw_file:\s*(.+)', content)
    if m:
        raw = m.group(1).strip().strip('"')
        fname = os.path.basename(raw)
        claimed_raw_files.add(fname)
    else:
        sources_without_rawfile.append(os.path.basename(fpath))

# 所有clipping文件
clip_files = set(f for f in os.listdir(clip_dir) if f.endswith('.md'))

print(f'Sources含raw_file字段: {len(claimed_raw_files)}')
print(f'Sources无raw_file字段: {len(sources_without_rawfile)}')
print(f'Clipping文件总数: {len(clip_files)}')
print()

# 找出clipping文件没有对应source raw_file声明
unmatched = clip_files - claimed_raw_files
print(f'没有source声明的clipping文件: {len(unmatched)}')
for f in sorted(unmatched):
    print(f'  {f}')

print()
print('=== Sources无raw_file字段（可能是新格式或缺字段）===')
for f in sorted(sources_without_rawfile):
    print(f'  {f}')

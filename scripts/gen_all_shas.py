import hashlib, os

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

clip_dir = r'd:\AI\LLM-WIKI\jiaruo\raw\clippings'
out_path = r'd:\AI\LLM-WIKI\jiaruo\scripts\all_shas.txt'

with open(out_path, 'w', encoding='utf-8') as out:
    for fname in sorted(os.listdir(clip_dir)):
        if fname.endswith('.md'):
            fpath = os.path.join(clip_dir, fname)
            sha = sha256_file(fpath)
            out.write(f'{sha}  {fname}\n')

print('Done. Written to all_shas.txt')

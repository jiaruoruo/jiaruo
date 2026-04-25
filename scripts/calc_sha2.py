# -*- coding: utf-8 -*-
import hashlib, os

base = r'd:\AI\LLM-WIKI\jiaruo\raw\pdfs'
results = []
for f in os.listdir(base):
    if not f.endswith('.pdf'):
        continue
    path = os.path.join(base, f)
    h = hashlib.sha256()
    with open(path, 'rb') as fp:
        for chunk in iter(lambda: fp.read(65536), b''):
            h.update(chunk)
    results.append((h.hexdigest(), f))

out_path = r'C:\Users\jiaruo\sha_output2.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    for digest, name in sorted(results, key=lambda x: x[1]):
        out.write(f'{digest}  {name}\n')

print('Done')

# -*- coding: utf-8 -*-
import hashlib, os, glob

target_dir = 'raw/clippings'
files = [
    'raw/clippings/MCU-LESS.md',
    'raw/articles/MCU-LESS.md',
]
# Also add date-prefixed new files
for f in sorted(glob.glob('raw/clippings/2026-05-1*.md')):
    files.append(f)

for path in files:
    if not os.path.exists(path):
        print(f'NOT FOUND: {path}')
        continue
    h = hashlib.sha256()
    with open(path, 'rb') as fp:
        for chunk in iter(lambda: fp.read(65536), b''):
            h.update(chunk)
    import datetime
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d')
    print(f'SHA256: {h.hexdigest()}  mtime={mtime}  {path}')

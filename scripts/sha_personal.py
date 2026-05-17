# -*- coding: utf-8 -*-
import hashlib, os, glob

files = sorted(glob.glob('raw/personal/*.md') + glob.glob('raw/personal/*.html'))
for path in files:
    h = hashlib.sha256()
    with open(path, 'rb') as fp:
        for chunk in iter(lambda: fp.read(65536), b''):
            h.update(chunk)
    sz = os.path.getsize(path)
    mtime = __import__('datetime').datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d')
    print(f'{h.hexdigest()}  size={sz}  mtime={mtime}  {path}')

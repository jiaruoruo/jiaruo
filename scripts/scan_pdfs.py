import os, hashlib, glob

BASE = r'd:\AI\LLM-WIKI\jiaruo'
results = []
for p in sorted(
    glob.glob(os.path.join(BASE, 'raw/pdfs/*.pdf')) +
    glob.glob(os.path.join(BASE, 'raw/pdfs/**/*.pdf'), recursive=True)
):
    h = hashlib.sha256(open(p,'rb').read()).hexdigest()[:8]
    sz = os.path.getsize(p) // 1024
    rel = p.replace(BASE + os.sep, '').replace('\\', '/')
    results.append(f"{h} {sz:5d}KB {rel}")

out = os.path.join(BASE, 'scripts', 'pdf_scan.txt')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results) + '\n')
print(f"Wrote {len(results)} entries to {out}")

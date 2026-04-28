import hashlib
from pathlib import Path

new_shas = ['dd1ba0a0','fb082278','e3960997','b6697bab','9c17ce58','304dbdfa','f28dd641','8bb89b94','1405e3c9']
clippings = Path('raw/clippings')
out = open('scripts/new_clippings_combined.txt', 'w', encoding='utf-8')
count = 0
for f in sorted(clippings.glob('*.md')):
    sha = hashlib.sha256(f.read_bytes()).hexdigest()[:8]
    if sha in new_shas:
        out.write(f'=== FILE: {f.name} (SHA:{sha}) ===\n')
        out.write(f.read_text(encoding='utf-8'))
        out.write('\n\n')
        count += 1
        print(f'Written: {f.name}')
out.close()
print(f'Total: {count} files')

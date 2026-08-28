
import os

output_path = r'd:\AI\LLM-WIKI\jiaruo\prt_analysis.txt'

with open(output_path, 'w', encoding='utf-8') as out:
    for fname in ['z2_asm1.prt', 'g2_model1.prt', 'tuojia_model1.prt']:
        fpath = f'D:/jiaruo/Desktop/文件转换/{fname}'
        with open(fpath, 'rb') as f:
            data = f.read()
        out.write(f'\n{"="*60}\n')
        out.write(f'FILE: {fname}  ({len(data)} bytes)\n')
        out.write(f'{"="*60}\n')
        out.write('--- First 256 bytes hex ---\n')
        for i in range(0, min(256, len(data)), 16):
            chunk = data[i:i+16]
            hex_part = ' '.join(f'{b:02x}' for b in chunk)
            asc_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
            out.write(f'{i:04x}: {hex_part:<48}  {asc_part}\n')
        out.write('\n--- Extracted strings (len>=6) ---\n')
        strings = []
        current = ''
        spos = 0
        for i, b in enumerate(data):
            if 32 <= b < 127:
                if not current: spos = i
                current += chr(b)
            else:
                if len(current) >= 6:
                    strings.append((spos, current))
                current = ''
        if current and len(current) >= 6:
            strings.append((spos, current))
        seen = set()
        cnt = 0
        for p, s in strings:
            if s not in seen and cnt < 80:
                seen.add(s)
                out.write(f'  @{p:06x}: {repr(s)}\n')
                cnt += 1
        out.write(f'\n  Total unique strings found: {cnt}\n')

print(f'Analysis written to: {output_path}')

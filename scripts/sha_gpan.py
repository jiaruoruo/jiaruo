import hashlib, os

files = [
    'raw/pdfs/GE1101芯片应用介绍_V0.1.pdf',
    'raw/pdfs/GE1101用户使用手册_V0.1.pdf',
    'raw/pdfs/Goodix GPAN Presentation for 车载通信(1).pdf',
    'raw/pdfs/MCULess方案调研.pdf',
    'raw/pdfs/MCULess方案进展介绍.pdf',
    'raw/pdfs/MCULess Based ZCU验证.pdf',
    'raw/pdfs/MCULess方案验证（关键技术点和验证范围）.pdf',
    'raw/pdfs/MCULess验证汇报.pdf',
    'raw/pdfs/售前方案-理想GPAN座椅v1.1.pdf',
    'raw/pdfs/基于GPAN的MCULess BZCU(第一阶段)_硬件设计简要说明V0.94_20250828.pdf',
]

results = []
for f in files:
    if os.path.exists(f):
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        results.append(f'{h}  {f}')
    else:
        results.append(f'NOT FOUND: {f}')

output = '\n'.join(results)
print(output)
with open('scripts/sha_gpan_output.txt', 'w', encoding='utf-8') as out:
    out.write(output + '\n')
print('Written to scripts/sha_gpan_output.txt')

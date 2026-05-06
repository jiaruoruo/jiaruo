import hashlib, os, sys

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

clip_dir = r'd:\AI\LLM-WIKI\jiaruo\raw\clippings'

files_to_check = [
    '2026-04-25标量、矢量(向量)、张量（tensors）的理解.md',
    '2026-04-28MCU-less架构在汽车电子中的实现路径深度解析.md',
    '2026-04-28下一代汽车电子架构革命：MCU Less技术如何重塑区域控制器设计？.md',
    '2026-04-28从分布式ECU到MCU-less边缘节点的技术演进之路.md',
    '2026-04-28汽车ECU的MCU-less变革：从分布式走向中央计算的关键路径.md',
    '2026-04-28硬件极简化革命：从传统ECU到MCU-less边缘节点的设计变革.md',
    '2026-04-28聊一聊MCULess, 10BASE-T1S以及RCP.md',
    '2026-04-28车灯技术迎来新变革？MCU-Less方案正在重新定义智能车灯.md',
    '2026-04-28车身(区域)研究：ZCU搭载量超200万辆，向"即插即用"模块化平台演进.md',
    '2026-04-28软件定义汽车的背后：一场架构的"深层次革命".md',
    '2026-05-022026北京车展新能源汽车电子电器架构总结、技术对标及应用解析.md',
    '2026-05-02特斯拉公开五份灵巧手专利，"最难部分"难在哪里？.md',
    '2026-05-02荣耀机器人背后，7家中国供应商！.md',
    '2026-05-0510BASE-T1S技术深度解析与汽车电子架构革命.md',
    '2026-05-0510BASE-T1S汽车以太网技术深度解析.md',
    '2026-05-05PoDL技术在汽车以太网供电的创新应用.md',
    '2026-05-05RCP协议深度解析：MCU-less架构下如何实现远程硬件控制.md',
    '2026-05-05RCP远程控制协议的革命性创新：汽车电子架构的范式转移.md',
    '2026-05-05汽车以太网技术深度解析：从10BASE-T1S到1000BASE-T1的全面演进.md',
    '2026-05-05软件定义汽车时代：RCE边缘节点与区域架构的深度变革.md',
    'MCULess调研报告.md',
    'MCU-LESS.md',
]

out_path = r'd:\AI\LLM-WIKI\jiaruo\scripts\shas_result.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    for fname in files_to_check:
        fpath = os.path.join(clip_dir, fname)
        if os.path.exists(fpath):
            sha = sha256_file(fpath)
            out.write(f'{sha}  {fname}\n')
            print(f'OK: {fname[:40]}...')
        else:
            out.write(f'NOT FOUND: {fname}\n')
            print(f'NOT FOUND: {fname}')
print('Done. Written to shas_result.txt')

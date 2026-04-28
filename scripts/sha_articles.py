import hashlib, os

# 可读格式文件（md / html / docx）
readable = [
    'raw/articles/MCU-LESS.md',
    'raw/articles/EtherCAT_GPAN_Validation_Design.html',
    'raw/articles/GPAN_MCULess_验证报告.html',
    'raw/articles/GPAN芯片规格介绍文档_V0.2 2025-08-05.docx',
    'raw/articles/GPAN部分功能澄清文档_V4.1.docx',
]
# 二进制格式（pptx / xlsx / vsdx）—— 只计算哈希，不创建 source 页
binary = [
    'raw/articles/GPAN 车载MCULess和分布式音频介绍(1.8).pptx',
    'raw/articles/GPAN 车载通信介绍-应用场景价值分析(0.8).pptx',
    'raw/articles/GPAN 车载通信介绍-应用场景价值分析0.6.pptx',
    'raw/articles/GPAN应用场景--外发理想.vsdx',
    'raw/articles/MCU-Less 座椅项目讨论_20260305-V0.5.pptx',
    'raw/articles/成本核算0.4 -- 公共.xlsx',
]

print("=== READABLE ===")
for f in readable:
    if os.path.exists(f):
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        print(f"{h}  {f}")
    else:
        print(f"NOT FOUND: {f}")

print("\n=== BINARY (hash only) ===")
for f in binary:
    if os.path.exists(f):
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        print(f"{h}  {f}")
    else:
        print(f"NOT FOUND: {f}")

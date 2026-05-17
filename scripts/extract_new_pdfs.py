"""提取新增 PDF 的文本内容（前 3 页），输出到 scripts/new_pdfs_text.txt"""
import os, hashlib

try:
    import pdfplumber
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdfplumber', '-q'])
    import pdfplumber

BASE = r'd:\AI\LLM-WIKI\jiaruo'

NEW_PDFS = [
    r'raw/pdfs/【报告7670】汽车传感器市场调研.pdf',
    r'raw/pdfs/芯片企业合集/ARM体系结构详解(我上课时老师的100多页PPT课件).pdf',
    r'raw/pdfs/芯片企业合集/ARM嵌入式系统ARM芯片的应用和选型.pdf',
    r'raw/pdfs/芯片企业合集/ARM常用ARM芯片选型.pdf',
    r'raw/pdfs/芯片企业合集/联发科MTK芯片型号资料大全.pdf',
    r'raw/pdfs/芯片企业合集/联发科SDK资料.pdf',
    r'raw/pdfs/芯片企业合集/高通芯片发展规格.pdf',
    r'raw/pdfs/芯片企业合集/高通芯片最强介绍.pdf',
    r'raw/pdfs/芯片制造/倒装芯片凸点制作方法.pdf',
    r'raw/pdfs/芯片制造/图解芯片制作工艺流程.pdf',
    r'raw/pdfs/芯片制造/柔性电子制造技术基础-第4讲-PART1-2014.pdf',
    r'raw/pdfs/芯片制造/芯片制造倒装焊工艺与设备解决方案.pdf',
    r'raw/pdfs/芯片封装测试/封装测试工艺教育资料.pdf',
    r'raw/pdfs/芯片封装测试/测试!芯片测试的意义.pdf',
    r'raw/pdfs/芯片封装测试/芯片封装引线电性能的测试.pdf',
    r'raw/pdfs/芯片封装测试/裸芯片封装技术的发展与挑战.pdf',
    r'raw/pdfs/芯片封装测试/集成电路封装和可靠性Chapter2-1-芯片互连技术.pdf',
    r'raw/pdfs/芯片设计/18微米芯片后端设计的相关技术.pdf',
    r'raw/pdfs/芯片设计/ECO技术在SoC芯片设计中的应用-王巍.pdf',
    r'raw/pdfs/芯片设计/LDO芯片设计报告及电路分析报告.pdf',
    r'raw/pdfs/芯片设计/一种基于MEMS技术的压力传感器芯片设计-王大军.pdf',
    r'raw/pdfs/芯片设计/半导体缺陷解析及中英文术语一览.pdf',
    r'raw/pdfs/芯片设计/射频芯片校准设计.pdf',
    r'raw/pdfs/芯片设计/常用存储器芯片设计指南.pdf',
    r'raw/pdfs/芯片设计/芯片研发过程介绍.pdf',
    r'raw/pdfs/芯片设计/芯片设计和生产流程.pdf',
    r'raw/pdfs/芯片设计/芯片设计流程.pdf',
    r'raw/pdfs/芯片设计/超大规模集成电路中低功耗设计与分析.pdf',
]

out_lines = []
for rel in NEW_PDFS:
    p = os.path.join(BASE, rel.replace('/', os.sep))
    sha = hashlib.sha256(open(p,'rb').read()).hexdigest()[:8]
    out_lines.append(f'\n{"="*70}')
    out_lines.append(f'FILE: {rel}')
    out_lines.append(f'SHA8: {sha}')
    try:
        with pdfplumber.open(p) as pdf:
            total = len(pdf.pages)
            out_lines.append(f'PAGES: {total}')
            text_parts = []
            for pg in pdf.pages[:4]:
                t = pg.extract_text()
                if t:
                    text_parts.append(t.strip())
            combined = '\n'.join(text_parts)[:3000]
            out_lines.append(f'TEXT (first 4 pages):\n{combined}')
    except Exception as e:
        out_lines.append(f'ERROR: {e}')

out_path = os.path.join(BASE, 'scripts', 'new_pdfs_text.txt')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print(f'Done. Output: {out_path}')

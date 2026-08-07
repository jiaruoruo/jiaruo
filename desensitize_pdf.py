"""
PDF 脱敏工具 v2 - 基于 RapidOCR（更快更轻量）
对扫描件PDF进行 OCR + 敏感信息识别 + 黑块遮盖

支持的脱敏类型（按公司规则）:
- 手机号: 保留前3位和后4位，如 139****8888
- 邮箱: 保留前缀前2位和@后缀，如 ch*****@qq.com
- 姓名: 保留姓氏，如 张*
- 地址: 保留到区县一级（整行遮盖）
- 身份证: 保留前1位和后1位
- 车牌号: 保留前2位，如 京A*****
"""

import sys
import os
import re
import fitz  # PyMuPDF
import numpy as np
import cv2
import time

sys.stdout.reconfigure(encoding='utf-8')

# ===================== 配置 =====================
PDF_INPUT  = r'd:\jiaruo\Downloads\打印-附件4-第三方检测报告（技术指标-整车应用指标-产业指标）_部分2.pdf'
PDF_OUTPUT = r'd:\jiaruo\Downloads\打印-附件4-第三方检测报告（技术指标-整车应用指标-产业指标）_部分2_脱敏.pdf'
RENDER_SCALE = 1.5   # 渲染倍率（1.5 在速度和精度间取得平衡）
# ================================================

print("初始化 RapidOCR（ONNX 推理引擎）...")
from rapidocr_onnxruntime import RapidOCR
engine = RapidOCR()
print("RapidOCR 初始化完成")


# ====== 敏感信息正则模式 ======
PATTERNS = [
    # 手机号: 1开头11位
    {
        'name': '手机号',
        'regex': re.compile(r'(?<!\d)1[3-9]\d{9}(?!\d)'),
        'mask_fn': lambda t: t[:3] + '****' + t[-4:],
    },
    # 邮箱
    {
        'name': '邮箱',
        'regex': re.compile(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'),
        'mask_fn': lambda t: (t.split('@')[0][:2] + '*****@' + t.split('@')[1]) if '@' in t else t,
    },
    # 身份证: 15位或18位（末位可为X）
    {
        'name': '身份证',
        'regex': re.compile(r'(?<!\d)\d{15}(?!\d)|(?<!\d)\d{17}[\dXx](?!\d)'),
        'mask_fn': lambda t: t[0] + '*' * (len(t) - 2) + t[-1],
    },
    # 中国车牌号
    {
        'name': '车牌号',
        'regex': re.compile(r'[\u4e00-\u9fff][A-Z][A-Z0-9·]{4,5}'),
        'mask_fn': lambda t: t[:2] + '*' * (len(t) - 2),
    },
]

# 中文姓名关键词（出现这些词后方紧跟 2-4 字中文视为姓名）
NAME_CONTEXT_PATTERN = re.compile(
    r'(编制|复核|批准|审核|测试工程师|联系人|负责人|姓名|报告人|授权签字人|验证人|校核人)[\s:：]*'
    r'([\u4e00-\u9fff]{2,4})'
)

# 地址关键词（出现这些词的整个文本框视为需要遮盖的地址）
ADDRESS_KEYWORDS = ['省', '市', '区', '县', '路', '街道', '号院', '楼', '室', '栋']
ADDRESS_CONTEXT_PATTERN = re.compile(
    r'([\u4e00-\u9fff]{2,4}[省市][\u4e00-\u9fff]{2,6}[区县])'
)


def find_sensitive_regions(ocr_results):
    """
    在OCR结果中查找敏感信息，返回需要遮盖的bbox列表
    ocr_results: RapidOCR返回的 [(box, text, score), ...]
    """
    regions = []
    
    for item in ocr_results:
        if item is None:
            continue
        # RapidOCR result item: (box, text, score)
        # box shape: [[x0,y0],[x1,y1],[x2,y2],[x3,y3]]
        box, text, score = item[0], item[1], item[2] if len(item) > 2 else 1.0
        if not text or not text.strip():
            continue
        clean = text.strip()
        
        hit = False
        
        # 1. 正则模式匹配
        for pat in PATTERNS:
            if pat['regex'].search(clean):
                print(f"    [{pat['name']}] {clean}")
                hit = True
                break
        
        # 2. 姓名检测（关键词上下文）
        if not hit and NAME_CONTEXT_PATTERN.search(clean):
            print(f"    [姓名] {clean}")
            hit = True
        
        # 3. 地址检测
        if not hit and ADDRESS_CONTEXT_PATTERN.search(clean):
            print(f"    [地址] {clean}")
            hit = True
        
        if hit:
            regions.append(box)
    
    return regions


def box_to_rect(box, scale):
    """将OCR四边形box转换为PyMuPDF矩形 (PDF坐标)"""
    pts = np.array(box, dtype=float)
    x0 = pts[:, 0].min() / scale
    y0 = pts[:, 1].min() / scale
    x1 = pts[:, 0].max() / scale
    y1 = pts[:, 1].max() / scale
    # 扩大2pt确保完全覆盖
    return fitz.Rect(x0 - 2, y0 - 2, x1 + 2, y1 + 2)


def process_pdf():
    t0 = time.time()
    doc = fitz.open(PDF_INPUT)
    total_pages = doc.page_count
    print(f"\n开始处理 PDF（共 {total_pages} 页，渲染倍率 {RENDER_SCALE}x）...")

    total_redactions = 0

    for page_idx in range(total_pages):
        page = doc[page_idx]
        t_page = time.time()
        print(f"\n[{page_idx+1}/{total_pages}] 正在处理...", end=' ', flush=True)

        # 渲染页面为图像
        mat = fitz.Matrix(RENDER_SCALE, RENDER_SCALE)
        pix = page.get_pixmap(matrix=mat)
        img_bytes = pix.tobytes('png')

        # 转为 OpenCV numpy array
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # RapidOCR 推理
        result, elapse = engine(img)

        if not result:
            print(f"无文字，耗时 {time.time()-t_page:.1f}s")
            continue

        print(f"识别到 {len(result)} 个文字块，耗时 {time.time()-t_page:.1f}s")

        # 查找敏感区域
        sensitive_boxes = find_sensitive_regions(result)

        if not sensitive_boxes:
            print(f"  → 未发现敏感信息")
            continue

        print(f"  → 发现 {len(sensitive_boxes)} 处敏感信息，进行遮盖")

        # 绘制黑色矩形覆盖
        for box in sensitive_boxes:
            rect = box_to_rect(box, RENDER_SCALE)
            page.draw_rect(rect, color=(0, 0, 0), fill=(0, 0, 0))
            total_redactions += 1

    elapsed = time.time() - t0
    print(f"\n{'='*50}")
    print(f"处理完成！共遮盖 {total_redactions} 处敏感信息，总耗时 {elapsed:.0f}s")
    print(f"保存脱敏 PDF → {PDF_OUTPUT}")
    doc.save(PDF_OUTPUT)
    doc.close()
    print("完成！")


if __name__ == '__main__':
    process_pdf()

import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'd:\jiaruo\Downloads\打印-附件4-第三方检测报告（技术指标-整车应用指标-产业指标）_部分2.pdf'
print(f"File exists: {os.path.exists(pdf_path)}")
print(f"File size: {os.path.getsize(pdf_path)} bytes")

try:
    import fitz
    doc = fitz.open(pdf_path)
    print(f"Page count: {doc.page_count}")
    for i in range(min(5, doc.page_count)):
        p = doc[i]
        t = p.get_text()
        imgs = p.get_images()
        print(f"Page {i+1}: text_len={len(t.strip())}, images={len(imgs)}")
        if t.strip():
            print(f"  Text preview: {t[:200]}")
    doc.close()
except Exception as e:
    print(f"Error with fitz: {e}")

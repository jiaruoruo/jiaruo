import sys
import fitz
import os

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'd:\jiaruo\Downloads\打印-附件4-第三方检测报告（技术指标-整车应用指标-产业指标）_部分2.pdf'
out_dir = r'd:\AI\LLM-WIKI\jiaruo\pdf_previews'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {doc.page_count}")

# Save first 3 pages as images
for i in range(min(3, doc.page_count)):
    page = doc[i]
    mat = fitz.Matrix(1.5, 1.5)  # Scale factor for better resolution
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(out_dir, f'page_{i+1}.png')
    pix.save(out_path)
    print(f"Saved page {i+1} -> {out_path}")

doc.close()
print("Done.")

# -- coding: utf-8 --
from PyPDF2 import PdfFileReader, PdfFileWriter
# 1. 获取原始pdf文件
fp_read_file = open("2020年CPA会计考试重难点.pdf", 'rb')
# 2. 将要分割的PDF内容格式化
pdf_input = PdfFileReader(fp_read_file)
# 3. 实例一个 PDF文件编写器
pdf_output = PdfFileWriter()
# 4. 把67到 78页放到PDF文件编写器
for i in range(67, 79):
    pdf_output.addPage(pdf_input.getPage(i))
# 5. PDF文件输出
with open("第9章.pdf", 'wb') as pdf_out:
    pdf_output.write(pdf_out)
print("PDF切分完成")

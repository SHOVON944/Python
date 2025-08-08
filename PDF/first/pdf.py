import os
from PyPDF2 import PdfMerger

# ফাইল পাথ সেট করুন
file_path = "E:/Study/Document/Python/"

merger = PdfMerger()
merger.append(os.path.join(file_path, "a.pdf"))
merger.append(os.path.join(file_path, "b.pdf"))
merger.write(os.path.join(file_path, "merged.pdf"))
merger.close()
from PyPDF2 import PdfMerger

merge = PdfMerger()

files = ['a.pdf', 'b.pdf', 'c.pdf']

for file in files:
    merge.append(file)

merge.write("Merged.pdf")

merge.close
print("PDF merge successfully")
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("a.pdf")
merger.append("b.pdf")
merger.append("c.pdf")
merger.write("three.pdf")
merger.close()







# from PyPDF2 import PdfMerger

# merge = PdfMerger()

# files = ['a.pdf', 'b.pdf', 'c.pdf']

# for file in files:
#     merge.append(file)

# merge.write("Merged.pdf")

# merge.close
# print("PDF merge successfully")
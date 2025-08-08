from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("a.pdf")
merger.append("b.pdf")
merger.append("c.pdf")
merger.write("three.pdf")
merger.close()

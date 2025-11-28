from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("PHY - 122 (1, 2, 3).pdf")
merger.append("EXP -04 Flywheel.pdf")

merger.write("Combined.pdf")
merger.close()
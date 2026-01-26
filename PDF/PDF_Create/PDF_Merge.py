from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("1.pdf")
merger.append("2.pdf")
merger.append("3.pdf")
merger.append("4.pdf")
merger.append("5.pdf")
merger.append("6.pdf")
merger.append("7.pdf")
merger.append("8.pdf")
merger.append("9.pdf")
merger.append("10.pdf")
merger.append("11.pdf")
merger.append("12.pdf")
merger.append("13.pdf")
merger.append("14.pdf")
merger.append("15.pdf")
merger.append("16.pdf")

merger.write("Prev(L-2, S-I).pdf")
merger.close()
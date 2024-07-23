from PyPDF2 import PdfFileMerger

pdfs = ['output1.pdf', 'output2.pdf']  # list of pdfs to merge

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")  # output pdf file
merger.close()

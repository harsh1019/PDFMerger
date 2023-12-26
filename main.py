import PyPDF2

pdFiles = ["sample1.pdf", "sample2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdFiles:
    pdfile = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfile)
    merger.append(pdfReader)
    pdfile.close()

merger.write('merged.pdf')
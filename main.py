from PyPDF2 import PdfWriter, PdfReader

def merger_pdfs(paths, outfile):
    pdfw = PdfWriter()
    
    for path in paths:
        pdfr = PdfReader(path)
        for i in range(len(pdfr.pages)):
            pdfw.add_page(pdfr.pages[i])
    
    with open(outfile, 'wb') as out:
        pdfw.write(out)
        
if __name__ == "__main__":
    paths = ['Git & Github.pdf', 'Schedule for josaa.pdf']
    merger_pdfs(paths, 'merger.pdf')


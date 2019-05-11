import PyPDF2 


def pdfTextExtract(filename):
    
    pdfObjRAW = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObjRAW)
    rawText = ""
    for i in range(pdfReader.numPages):
        pageObjRaw = pdfReader.getPage(i)
        rawText += pageObjRaw.extractText() + " "
    print(rawText.strip())
    

def tesFunction():
    pdfTextExtract("Omolola Barbra Birch Work Permit.pdf")

tesFunction()
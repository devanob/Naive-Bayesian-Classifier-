import PyPDF2 


def pdfTextExtract(filename):
    
    pdfObjRAW = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObjRAW)
    rawText = ""
    for i in range(pdfReader.numPages):
        pageObjRaw = pdfReader.getPage(i)
        rawText += pageObjRaw.extractText() + " "
    text = rawText.strip()
    if text:
        return text
    
    

def tesFunction():
    print(pdfTextExtract("JD Policy and Advocacy Officer.pdf"))

tesFunction()
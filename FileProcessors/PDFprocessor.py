import PyPDF2 


def pdfTextExtract(filename):
    
    pdfObjRAW = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObjRAW)
    rawText = ""
    for i in range(pdfReader.numPages):
        pageObjRaw = pdfReader.getPage(i)
        rawText += pageObjRaw.extractText() + " "
    if rawText:
        return rawText
    
    

def tesFunction():
    print(pdfTextExtract("JD Policy and Advocacy Officer.pdf"))

if __name__ == '__main__':
    tesFunction()
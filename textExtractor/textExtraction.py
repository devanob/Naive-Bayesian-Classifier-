
from PDFprocessor  import pdfTextExtract
import pickle
from collections import Counter
contractions = open("Important/contractions.pickle","rb")
contractions = pickle.load(contractions)
import string
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))
class textExtractionProcessor:
    
    text = ""
   
    def setText(self, text):
        self.text = text

    def removeNonAscii(self):
        tempString = ""
        tempString = ''.join(ch for ch in self.text  if ord(ch)< 256)
        self.text = tempString
    def removeInternelTrailingSpaces(self):
        tempList = self.text.split() #split by space character
        tempList = [word for word in tempList if  word.strip()]
        self.text = ' '.join(tempList)

    def generalProcessing(self):
        #split the string based on space character
        tempListWords = self.text.split()
        for word in tempListWords:
            if word.lower() in contractions:
                self.text = self.text.replace(word, contractions[word.lower()])
            if not word.islower():
                self.text = self.text.replace(word, word.lower())
        ##replit the text
        
            

        self.text = self.text.translate(str.maketrans(string.punctuation, " "*len(string.punctuation), ''))
        self.removeInternelTrailingSpaces()
        #remove numbers, words less than two chracter and stopping words
        filtered_sentence = [word for word in self.text.split() if not (word in stop_words or  word.isdigit() or len(word) < 2) ]
        self.text = " ".join(filtered_sentence)
        

        ##not process contractions 
    def processText(self):
        if not self.text: ## if the text is empty then do nothing
            return
        ##remove trailing spaces from both end of the string 
        self.text = self.text.strip()
        
        ##remove any special or non ascii characters
        ##self.removeNonAscii()

        #remove unnessary  internel spaces in the  tex
        self.removeInternelTrailingSpaces()

        #generalProcessingNow
        self.generalProcessing()

    def getProcessedText(self):
        pass
    
    def getText(self):
        return self.text


##Test Function Module
if __name__ == '__main__':
    testExtraction = textExtractionProcessor()
    testText =  pdfTextExtract("How to Write_14.pdf")
    testExtraction.setText(testText)
    testExtraction.setText(testText)
    testExtraction.processText()
    print(Counter(testExtraction.getText().split()))
    
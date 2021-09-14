'''
Created on 15-Sep-2021

@author: hemalatha
'''

if __name__ == '__main__':
    pass

#THIS PROGRAM IS USED TO CNVERT PDF TO SPEECH
import pyttsx3 # MODULE FOR TXT & SPEECH PURPOSE
speak=pyttsx3.init()# INITIALIZE MODULE
import pyPDF2
book=open('oops.pdf','rb')#arguements('pdfname.pdf','rb')
pdfReader=pyPDF2.pdffilereader(book)
pages=pdfReader.numPages#to know total no.of.pages in pdf
print(pages)
p_g=pdfReader.getPage(7)#page no from where to started
text=p_g.extractText()
speak.say() #CONVERTION USNG INBUILT METHOD
speak.runAndWait()#Execution

#AND ONE MORE METHOD-TO READ ICLUDE START PAGE AND END PAGE
import pyttsx3 
import pyPDF2
book=open('oops.pdf','rb')#arguements('pdfname.pdf','rb')
pdfReader=pyPDF2.pdffilereader(book)
pages=pdfReader.numPages#to know total no.of.pages in pdf
print(pages)
for num in range(7,pages):
    p_g=pdfReader.getPage(7)#page no from where to started
    text=p_g.extractText()
    speak.say() #CONVERTION USNG INBUILT METHOD
    speak.runAndWait()#Execution



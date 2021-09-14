'''
Created on 15-Sep-2021

@author: hemalatha
'''

if __name__ == '__main__':
    pass

#THIS PROGRAM IS USED TO CNVERT TEXT TO SPEECH
import pyttsx3 # MODULE FOR TXT & SPEECH PURPOSE

speak=pyttsx3.init()# INITIALIZE MODULE
speak.say('hello welcome to projects') #CONVERTION USNG INBUILT METHOD
speak.runAndWait()#EXECUTION

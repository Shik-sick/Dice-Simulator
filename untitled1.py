# -*- coding: utf-8 -*-
import PyPDF2

a=PyPDF2.PdfFileReader('pdf101.pdf')
#print(a.documentInfo)
#print(a.getNumPages())
str=""
for i in range(1,5):
    str+=a.getPage(i).extractText()
    
with open("text.txt","w",encoding='utf-8')as f:
    f.write(str)
    




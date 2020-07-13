# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:33:46 2020

@author: nikko
"""


inpString = input("Введите предложение: ")
myList = inpString.split()

strNum = 1

for el in myList:
    if(len(el)<=10):
        print(strNum, ": ", el)
    else:
        print(strNum, ": ", el[:10])
    
    strNum+=1

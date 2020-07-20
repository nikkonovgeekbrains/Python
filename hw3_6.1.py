# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:18:35 2020

@author: nikko
"""

def int_func(argStr):
    
    return argStr.capitalize()

    
inpStr = input ("Введите слово: ")
print ("Слово с заглавной буквы:", int_func(inpStr))
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:26:58 2020

@author: nikko
"""

def int_func(argStr):
    
   return argStr.capitalize()

 
    

inpStr = input ("Введите предложение: ")
listStr = inpStr.split()
upperStr = ""
for el in listStr:
    upperStr =  upperStr + int_func(el)+ " "
    #print (int_func(el))
print ("Предложение со словами с заглавной буквы: ", upperStr)
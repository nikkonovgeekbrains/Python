# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:30:23 2020

@author: nikko
"""

myList = []

el_count = int(input("Введите кол-во эл-тов в списке: "))
for el in range(el_count):
    myList.append(input(f"Введите элемент списка с номером {el}: "))

num =1    
print ("Исходный список: ", myList)
while (num<len(myList)):
        myList[num-1], myList[num] =  myList[num], myList[num-1]
        num+=2
        
print ("Преобразованный список: ", myList)        
        
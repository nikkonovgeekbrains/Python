# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:06:25 2020

@author: nikko
"""
num = 1

goodsList = []


while(True):
    name = input("Введите имя: ")
    coast = input("Введите стоимость: ")
    count = input("Введите количество: ")
    units = input("Введите единицы измерения: ")
    
    temp_dict = {"название":name, "цена":coast, "количество":count, "eд.":units}
    tempkort = (num, temp_dict)
    goodsList.append(tempkort)
    num+=1
    answ = input ("Хотите внести еще один товар? (y/n)")
    
    if (not(answ == "y" or answ == "Y") ): break

print (goodsList)

nameList = []
coastList = []
countList = []
unitsList = []

for el in goodsList:
    nameList.append(el[1].get("название"))
    coastList.append(el[1].get("цена"))
    countList.append(el[1].get("количество"))
    unitsList.append(el[1].get("eд."))

Analitic_dict = {"название":nameList, "цена":coastList, "количество":countList, "eд.":unitsList}
print(Analitic_dict)    
    
print ("End!")
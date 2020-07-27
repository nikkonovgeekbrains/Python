# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:12:25 2020

@author: nikko
"""

import re

myList = []
with open("text_6.txt", "r", encoding="utf-8") as f1:
    for line in f1:
        myList.append(line.split())
    print(myList)    

myDict = {}
for el in myList:
    print(len(el))
    name = el[0][0:len(el[0])-1]
    count = 0
    print(name)
    num = 0
    for i in range(1, len(el)):
        if(len(re.findall(r'[0-9]+', el[i]))>0):
            num += int(re.findall(r'[0-9]+', el[i])[0])
    print(f"Количество {name} равно {num}")
    myDict.update({f"{name}" : num})
    
print(f"Получили словарь: {myDict}")
        
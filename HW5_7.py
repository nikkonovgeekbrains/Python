# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:57:03 2020

@author: nikko
"""

import json


myList = []
with open("text_7.txt", "r", encoding="utf-8") as f1:
    for line in f1:
        myList.append(line.split())
    print(myList)

firmDict = {}
sumProf = 0 
numProf = 0
for el in myList:
    profit = float(el[2])-float(el[3])
    firmDict.update({f"{el[0]}":profit})
        
print(firmDict)


meanProf = sum([el for el in firmDict.values() if float(el) >= 0])/len([el for el in firmDict.values() if float(el) >= 0])
profDict = {"average_profit": meanProf}
print(profDict)

with open("my_file_7.json", "w", encoding="utf-8") as write_f:
    json.dump([firmDict, profDict], write_f, ensure_ascii=False)
        
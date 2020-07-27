# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:41:11 2020

@author: nikko
"""


with open("text_4.txt", "r", encoding= "utf-8") as f1:
    myList = []
    myDict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре", 
              "Five":"Пять", "Six":"Шесть", "Seven":"Семь", "Eight":"Восемь", "Nine":"Девять"}
    for line in f1:
        myList.append(line.split())
    print(myList)
    
    for steEl in myList:
        for i in range(len(steEl)):
            if myDict.get(steEl[i])!=None:
                steEl[i] = myDict.get(steEl[i])
    print(myList)
    with open("my_file_4.txt", "w", encoding= "utf-8") as f2:
        for el in myList:
            f2.write(' '.join(el)+"\n")
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:27:15 2020

@author: nikko
"""


class OurIsNotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt
        
myList = []
while(True):
    try:
        newEl = input("Введите следующий элемент списка: ")
        if newEl.lower() == "stop":
            break
        if newEl.isdigit()==False:
            raise OurIsNotDigit("Введенная стока не является числом!")
        myList.append(int(newEl))
    except OurIsNotDigit  as err:
        print(err)
    print (f"Текущий список: {myList}")

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:16:54 2020

@author: nikko
"""


season = ["winter", "winter", "spring","spring",
          "spring", "summer", "summer", "summer",
          "autumn", "autumn", "autumn", "winter"]

seasonDict = {1:"winter", 2:"winter", 3:"spring",  
             4:"spring", 5:"spring", 6:"summer",
             7:"summer", 8:"summer",  9:"autumn", 
             10:"autumn", 11:"autumn", 12:"winter"}

month = int(input("Введите номер месяца: "))
if (month>0 and month<=12 ):
    print("Время года (через  список): ", season[month-1])
    print("Время года (через  словарь): ", seasonDict.get(month))
else:
    print("Некорректный ввод данных!")
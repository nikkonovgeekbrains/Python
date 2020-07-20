# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:14:58 2020

@author: nikko
"""

def myPrintInfo(surname, name, year, city, email):
    print(f"Пользователь {surname} {name} родился в {year} году в городе {city}, адрес электронной почты : {email}") 
    
myUser = {"usName": "Nikolay", "usSurname": "Konovaltsev", "usYearOfBirth": 1994, "UsCity": "Moscow", "usEmail":"nikkonov@mail.ru" }

myPrintInfo(name = myUser.get("usName"), surname = myUser.get("usSurname"), email = myUser.get("usEmail"),
            city = myUser.get("UsCity"), year = myUser.get("usYearOfBirth"))
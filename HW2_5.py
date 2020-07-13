# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:06:08 2020

@author: nikko
"""


startList = [7, 5, 3, 3, 2]

print(startList)

while(True) :
    temp = True
    while temp == True:
        try:
            userNumber = int(input("Введите число: "))
            if userNumber < 1:
                print("Вы ввели не натуральное число!")
            else :
                temp = False
        except Exception:
            print("Вы ввели не натуральное число!")
    temp2 = 0

    while userNumber < startList[temp2]:
        temp2 = temp2 + 1
        if temp2 == len(startList) :
            break
    if temp2 == len(startList) :
        startList.append(userNumber)
    else:
        startList.insert(temp2, userNumber)

    print(startList)
    
    answ = input("Не хотите продолжать?(y/n) ")
    if (not(answ == "y" or answ == "Y") ): break
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:17:03 2020

@author: nikko
"""


def myFunc (tempSum):
    fl  = True
    sum1 = tempSum
    inpStr = str(input ("Введите последовательность чисел: "))
    inpList = inpStr.split()
    print (inpList)
    for el in inpList:
        if(not el.isdigit()):
            fl = False
            break
        sum1 = sum1+float(el)
    return sum1, fl


genSum = 0
complFl = True
while(True):
       
    genSum, complFl = myFunc(genSum)
    
    if (not(complFl)): break
    
    answ = input ("Хотите внести еще одну последовательность? (y/n)")
    
    if (not(answ.upper() == "Y") ): break
    
print ("Общая сумма чисел равна: ", genSum)  
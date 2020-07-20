# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:49:38 2020

@author: nikko
"""
def sumMaxFunc(n1, n2, n3):
    tempList = [n1, n2, n3]
    tempList.sort()
    return tempList[1]+tempList[2]

myList = []

for i in range(3):
    myList.append(float(input("Введите число: ")))

print ("Сумма двух наибольших чисел равна ", str(sumMaxFunc(myList[0], myList[1], myList[2])))   

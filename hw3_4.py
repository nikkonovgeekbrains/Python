# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:00:21 2020

@author: nikko
"""

def expFunc(num, deg):
    temp = 1
    for i in range(abs(deg)):
        temp = temp/num
    return temp  
def expStdFunc(num, deg):
    return num**deg

n1 = float(input("Введите число: "))
n2 = int(input("Введите степень (должна быть целым отрицательным числом): "))

print ("Результат возведения в степень: ", expFunc(n1,n2))
print ("Результат возведения в степень (через  стандартную функцию): ", expStdFunc(n1,n2))
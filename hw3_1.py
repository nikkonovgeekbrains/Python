# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:43:45 2020

@author: nikko
"""


def myFunc(num1, num2):
    if(num2==0):
        print("Ошибка! Деление на ноль невозможно.")
    else:
        return num1/num2

n1 = float(input('Введите первое число: '))
n2 = float(input('Введите второе число: '))

print("Результат деления:", str(myFunc(n1,n2)))
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:11:25 2020

@author: nikko
"""
class OurZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    num1 = float(input("Введите первое число:"))
    num2 = float(input("Введите второе число:"))
    if num2 ==0:
        raise OurZeroDivisionError("Знаменатель не должен равняться нулю!")
    print(f"Результат деления равен {num1/num2}")
except OurZeroDivisionError  as err:
    print(err)
    
except ValueError:
    print("Вы ввели не число!")
    
    
    
    
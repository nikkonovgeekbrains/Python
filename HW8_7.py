# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:34:49 2020

@author: nikko
"""


class CompNum:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
        
    def __str__(self):
        if self.Im >= 0:
            return f"{self.Re} + j{self.Im}"
        else:
            return f"{self.Re} - j{abs(self.Im)}"
        
    def __add__(self, other):
        return CompNum(self.Re + other.Re, self.Im + other.Im)
    
    def __mul__(self, other):
        return CompNum(self.Re * other.Re - self.Im * other.Im , self.Re * other.Im + self.Im * other.Re)

n1 = CompNum(1,1)
n2 = CompNum(-1,-1)
n3 = n1 + n2
n4 = n1 * n2

print(n1)
print(n2)
print(n3)
print(n4)
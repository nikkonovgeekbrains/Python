# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:09:42 2020

@author: nikko
"""


class Cell:
    def __init__(self, count):
        self.count = count
        
    def __str__(self):
        return str(self.count)
        
    def __add__(self, other):
        return Cell(self.count + other.count)
    
    def __sub__(self, other):
        if (self.count - other.count >= 0):
            return Cell(self.count - other.count)
        else:
            print("Невозможно выполнить вычитание!")
    
    def __mul__(self, other):
        return Cell(self.count * other.count)
    
    def __truediv__(self, other):
        try:
            return Cell(self.count / other.count)
        except Exception:
            print("Невозможно выполнить деление!")
    
    def make_order(self, row):
        tempStr = ""
        for i in range(self.count):
           tempStr+="*"
           if (i>0) and ((i+1)%row == 0):
               tempStr+="\n"
        return tempStr
    
cell1= Cell(13)
cell2 = Cell(5)

print(f"Кол-во ячеек суммарной клетки равно {cell1+cell2}")
if (cell1-cell2 != None): print(f"Кол-во ячеек разностной клетки равно {cell2-cell1}")
print(f"Кол-во ячеек перемноженной клетки равно {cell1*cell2}")
if (cell1/cell2 != None): print(f"Кол-во ячеек разностной клетки равно {cell1/cell2}")

print(f"Результат разбиения клетки:\n{cell1.make_order(5)}")




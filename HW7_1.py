# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:07:34 2020

@author: nikko
"""


class Matrix:
    def __init__(self, inpArr):
        self.inpArray = inpArr
        
    def __str__(self):
        tempStr = ""
        for i in range(len(self.inpArray)):
            for el in self.inpArray[i]:
                tempStr = tempStr + (f"{el}")
                tempStr+=" "
            tempStr+="\n"
        return tempStr
    
    def __add__(self, other):
        res = []
        for i in range(len(self.inpArray)):
            res.append([])
            for j in range(len(self.inpArray[i])):
                res[i].append(self.inpArray[i][j] + other.inpArray[i][j])
        return Matrix(res)
    
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[3,4,5],[6,7,8],[9,10,11]])
print(f"Первая матрица:\n{m1}")
print(f"Вторая матрица:\n{m2}")

m3 = m1+m2
print(f"Результат почленного суммирования двух матриц:\n{m3}")


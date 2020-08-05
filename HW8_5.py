# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:21:17 2020

@author: nikko
"""


class Warehouse:
    def __init__(self):
        self.eqList = [] #На складе
        self.eqOutList = [] #Было на складе, отдали
        
    def addEq(self, eq, count):
        if(eq.eqType == "Printer"):
            self.eqList.append({"Тип": eq.eqType, "Цена": eq.price, "Цвет": eq.color, "Цветность": eq.coloured, "Кол-во": count})
        elif (eq.eqType == "Scanner"):
             self.eqList.append({"Тип": eq.eqType, "Цена": eq.price, "Цвет": eq.color, "Разрешение": eq.dpi, "Кол-во": count})
        elif (eq.eqType == "Xerox"):
             self.eqList.append({"Тип": eq.eqType, "Цена": eq.price, "Цвет": eq.color, "Скорость отправки": eq.speed, "Кол-во": count})
             
    def outEq(self, num, place):
        if (num<= len(self.eqList)):
            self.eqOutList.append([self.eqList[num-1],place])
            self.eqList.pop(num-1)
        else:
            print("Некорректный ввод данных!")
class OfficeEquipment:
    def __init__(self, eqType, price, color, weight):
        self.eqType =eqType
        self.price = price
        self.color = color
        self.weight = weight
        
    
class Printer(OfficeEquipment):
    def __init__(self, price, color, weight, coloured=False):
        super().__init__("Printer",price, color, weight)
        self.coloured = coloured
    
class Scanner(OfficeEquipment):
    def __init__(self, price, color, weight, dpi=300):
        super().__init__("Scanner",price, color, weight)
        self.dpi = dpi
    
class Xerox(OfficeEquipment):
    def __init__(self, price, color, weight, speed):
        super().__init__("Xerox",price, color, weight)
        self.speed = speed
        
    
    
p1 = Printer(10000, "white", 5, True)
s1 = Scanner(8600, "black", 3, 500)
x1 = Xerox(12000, "blue", 7, 8)

w1 = Warehouse()
w1.addEq(p1,2)
w1.addEq(s1,4)
w1.addEq(x1,8)
print(w1.eqList)

w1.outEq(2, "Контора1")
print(w1.eqList)
print(w1.eqOutList)
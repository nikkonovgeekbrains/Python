# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:53:35 2020

@author: nikko
"""


class Warehouse:
    def __init__(self):
        pass
    
class OfficeEquipment:
    def __init__(self, price, color, weight):
        self.price = price
        self.color = color
        self.weight = weight
        
    
class Printer(OfficeEquipment):
    def __init__(self, price, color, weight, coloured=False):
        super().__init__(price, color, weight)
        self.coloured = coloured
    
class Scanner(OfficeEquipment):
    def __init__(self, price, color, weight, dpi=300):
        super().__init__(price, color, weight)
        self.dpi = dpi
    
class Xerox(OfficeEquipment):
    def __init__(self, price, color, weight, speed):
        super().__init__(price, color, weight)
        self.speed = speed
    
    
p1 = Printer(10000, "white", 5, True)
s1 = Scanner(8600, "black", 3, 500)
x1 = Xerox(12000, "blue", 7, 8)
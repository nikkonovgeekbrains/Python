# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:22:06 2020

@author: nikko
"""


class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def masCalc(self):
        return self.length * self.width * 25 *5 /1000
    
road =  Road(float(input("Введите длину дороги в метрах:")),float(input("Введите ширину дороги в метрах:")))

print(f"Для постройки дороги понадобится {road.masCalc()} т асфальта")


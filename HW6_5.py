# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:57:58 2020

@author: nikko
"""


class Stationery:
    def __init__(self,title):
        self.title = title    
    def draw(self):
        print("Запуск отрисовки (метод базового класса)")
        
class Pen(Stationery):
    def __init__(self):
        super().__init__("ручка")
        
    def draw(self):
        print(f"Запуск отрисовки (метод первого класса с именем {self.title})")

class Pencil(Stationery):
    def __init__(self):
        super().__init__("карандаш")    
    def draw(self):
        print(f"Запуск отрисовки (метод втого класса с именем {self.title})")
    
class Handle(Stationery):
    def __init__(self):
        super().__init__("маркер")
    def draw(self):
         print(f"Запуск отрисовки (метод третьего класса с именем {self.title})")
         
stationery1 = Pen()
stationery2 = Pencil()
stationery3 = Handle()

stationery1.draw()
stationery2.draw()
stationery3.draw()
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:23:26 2020

@author: nikko
"""
        
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage, "bonus":bonus}
                     
                    
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
      
    def get_full_name(self):
        return  self.name+ " " + self.surname
    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")
        
pos1 = Position("Николай", "Коновальцев", "инженер", 80000, 15000)
print(f"Полное имя: {pos1.get_full_name()} , доход с учетом премии: {str(pos1.get_total_income())}")
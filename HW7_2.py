# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:36:43 2020

@author: nikko
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    
    @abstractmethod
    def matCalc(self):
        pass
        
    @property
    def matCount(self):
        return round(self.matCalc(),2)
        
    
class Coat(Clothes):
      
    def matCalc(self):
        return self.param/6.5 + 0.5
    
class Suit(Clothes):
    def __init__(self, H):
        super().__init__(H)
      
    def matCalc(self):
        return 2*self.param + 3

    

c1 = Coat(2)
s1 = Suit(3)
print(f"На пальто ушло ткани: {c1.matCount}")
print(f"На костюм ушло ткани: {s1.matCount}")
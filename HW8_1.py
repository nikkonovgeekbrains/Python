# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:00:49 2020

@author: nikko
"""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
                
    
    @classmethod
    def extract(cls, data):
        day, month, year = data.split("-")
        
        return cls(int(day), int(month), int(year))
    
    @staticmethod
    def validation(day, month, year):
        if day>31 or day<1  or month>12 or month<1 or year>2020 or year<1990:
            print("Дата введена некорректно!")
        else:
            return f"{day}-{month}-{year}"
        


date_1 = Date.extract("10-11-1994")
print(date_1.validation(date_1.day, date_1.month, date_1.year))




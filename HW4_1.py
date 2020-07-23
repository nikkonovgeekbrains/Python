# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:57:42 2020

@author: nikko
"""
from sys import argv

script_name, userCoast, userHoursCount, userPremium = argv

def SalCalc(coast, hoursCount, premium):
   return coast * hoursCount + premium



#userCoast = 700
#userHoursCount = 160
#userPremium = 20000

print("Зарплата с учетом премии равна: ",SalCalc(float(userCoast), float(userHoursCount), float(userPremium)))
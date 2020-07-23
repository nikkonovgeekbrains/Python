# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:43:05 2020

@author: nikko
"""


krat_20_21_list = [el for el in range(20, 241) if el%20==0 or el%21==0]

print(krat_20_21_list)

#Второй способ:
krat_20_21_list_2 = sorted([el for el in range(20, 241, 20)] + [el for el in range(21, 241, 21)])

print(krat_20_21_list_2)
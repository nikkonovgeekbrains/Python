# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:54:13 2020

@author: nikko
"""


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_new_list = [el for el in my_list if my_list.count(el) == 1]

print(my_new_list)
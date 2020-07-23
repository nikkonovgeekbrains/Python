# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:36:34 2020

@author: nikko
"""


def factorial(num):
    res = 1
    for el in range(1, num+1):
        res *= el
        yield res

for el in factorial(5):
    print(el)
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:13:17 2020

@author: nikko
"""


from functools import reduce

print(reduce(lambda x, y: x * y,[el for el in range(100,1001,2)]))


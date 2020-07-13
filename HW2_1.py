# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:16:40 2020

@author: nikko
"""


user_list = (10,20.5, complex(1,2), "my string",b'bytes', True)

for el in user_list:
    print ('type of ', str(el), 'is', str(type(el)))
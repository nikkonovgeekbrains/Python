# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:23:11 2020

@author: nikko
"""


import itertools

def numGen(startNum):
    for el in itertools.count(startNum):
        if el > 10 :
            break
        else :
            print(el)
            
def cycleGen(inpStr):
    с = 0
    for el in itertools.cycle(inpStr):
        if с > 10 :
            break
        print(el)
        с += 1   


        
numGen(5)
cycleGen("Hello!")
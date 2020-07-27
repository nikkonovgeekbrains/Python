# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:46:48 2020

@author: nikko
"""



while(True):
    with open("my_file.txt", "a") as f1:
        inpStr = str(input("Введите строку (пустая для завершения):"))
        if inpStr == "": break
        f1.write(inpStr+"\n")
        
        
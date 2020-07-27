# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:08:44 2020

@author: nikko
"""


with open("my_file_2.txt", "r") as f1:
    num_of_str = 0
    for line in f1:
        num_of_str += 1
        num_of_word = len(line.split())
        print(f"В строке с номером {num_of_str} найдено {num_of_word} слов")
    
    print(f"В файле найдено {num_of_str} строк")
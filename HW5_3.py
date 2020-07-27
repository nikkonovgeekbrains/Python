# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:11:33 2020

@author: nikko
"""
import statistics

with open("text_3.txt", "r", encoding= "utf-8") as f1:
    workerList = []
    for line in f1:
        workerList.append(line.split())
    
    print(workerList)
    bigSalList = []
    
    bigSalList = [el for el in workerList if float(el[1]) >= 20000]
    
    print("Работники с зарплатой больше 20000:")
    numOfWorker = 1
    for el in bigSalList:
        print(f"{numOfWorker}) {el[0]} c зарплатой {el[1]}")
        numOfWorker+=1
    meanSal = statistics.mean([float(el[1]) for el in workerList ])
    print (f"Средняя зарплата всех сотрудников равна: {meanSal}")
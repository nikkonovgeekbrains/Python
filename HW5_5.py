# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:54:08 2020

@author: nikko
"""


with open("my_file_5.txt", "w") as f1:
    f1.truncate(0)

while(True):
    with open("my_file_5.txt", "a") as f1:
        inpNum = str(input("Введите число (пустой ввод для завершения):"))
        if inpNum == "": break
        f1.write(inpNum+" ")
        
        
with open("my_file_5.txt", "r") as f1:
    numList = [float(i) for i in (f1.read()).split()]
    
    #Второй способ
    #numList = list(map(float,(f1.read()).split()))   
    #print(numList)
    numSum = sum(numList)
    print (f"Сумма всех чисел равна: {round(numSum,2)}")
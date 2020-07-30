# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:00:30 2020

@author: nikko
"""
import time

class TrafficLight:
    
    def __init__(self):
        self.__color = "Red"
        
    
    def running (self):
        workTime = float(input("Введите время работы светофора в секундах: "))
        timeouts = {"Red":7, "Yellow":2, "Green":7}
        colorForm = {"Red":"\033[31m {}", "Yellow":"\033[33m {}", "Green":"\033[32m {}"}
        colors = ["Red", "Yellow", "Green", "Yellow"]
        count = 0
        startTime = time.time()
        while(True):
            if time.time()-startTime >= workTime:
                break
            self.__color = colors[count % 4]
            print(colorForm.get(self.__color) .format(self.__color))
            #print(self.__color)
            time.sleep(timeouts.get(self.__color))
            count+=1
        
tr = TrafficLight()
tr.running()    
      
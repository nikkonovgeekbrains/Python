# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:53:44 2020

@author: nikko
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def show_speed(self):
        print(f"Текущая скорость автомобиля: {str(self.speed)}")
    
    def go(self):
        print ("Машина поехала!")
        
    def stop(self):
        print ("Машина остановилась!")
    
    def turn(self,direct):
        print (f"Машина повернула {direct}!")

class TownCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed,color,"TownCar", False)
        
    def show_speed(self):
        if float(self.speed) <= 60:
            print(f"Текущая скорость автомобиля: {str(self.speed)}")
        else:
            print(f"Текущая скорость автомобиля: {str(self.speed)}- ПРЕВЫШЕНИЕ СКОРОСТИ!!!!")
        
class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed,color,"SportCar", False)
        
class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed,color,"WorkCar", False)
        
    def show_speed(self):
        if float(self.speed) <= 40:
            print(f"Текущая скорость автомобиля: {str(self.speed)}")
        else:
            print(f"Текущая скорость автомобиля: {str(self.speed)}- ПРЕВЫШЕНИЕ СКОРОСТИ!!!!")
        
class PoliceCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed,color,"PoliceCar", True)
        
townCar = TownCar(50,"green")
sportCar = SportCar(120,"red")
workCar = WorkCar(20,"white")
policeCar = PoliceCar(70,"black")

townCar.show_speed()
sportCar.show_speed()
workCar.show_speed()
policeCar.show_speed()

townCar.go()
sportCar.stop()
workCar.turn("направо")
policeCar.turn("налево")

print(f"Машина с азванием {townCar.name} цвета {townCar.color} едет со скоростью {townCar.speed}, принадлежность к полицейским: {townCar.is_police}")
print(f"Машина с азванием {sportCar.name} цвета {sportCar.color} едет со скоростью {sportCar.speed}, принадлежность к полицейским: {sportCar.is_police}")
print(f"Машина с азванием {workCar.name} цвета {workCar.color} едет со скоростью {workCar.speed}, принадлежность к полицейским: {workCar.is_police}")
print(f"Машина с азванием {policeCar.name} цвета {policeCar.color} едет со скоростью {policeCar.speed}, принадлежность к полицейским: {policeCar.is_police}")



class Car:
    def sound(self):
        print("Car sound is bad")

class Bike(Car):
    def sound(self):
        print("Bike Sound is good")

b = Bike()
b.sound()
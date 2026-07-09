from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass

class Worker(Employee, Eatable):
    def work(self):
        print("Worker is Working")

    def eat(self):
        print("Worker is Eating")

class Robot(Employee):
    def work(self):
        print("Robot is Working")

worker = Worker()
worker.work()
worker.eat()

robot = Robot()
robot.work()
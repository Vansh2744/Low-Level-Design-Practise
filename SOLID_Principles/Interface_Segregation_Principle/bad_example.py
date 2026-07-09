from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Worker(Employee):
    def work(self):
        print("Worker is Working")

    def eat(self):
        print("Worker is Eating")

class Robot(Employee):
    def work(self):
        print("Robot is Working")

    def eat(self):
        raise Exception("Robot can't Eat")


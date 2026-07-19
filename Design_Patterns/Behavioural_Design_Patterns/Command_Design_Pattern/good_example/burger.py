from command import Command
from chef import Chef

class Burger(Command):
    def __init__(self, chef:Chef):
        self.__chef = chef

    def cook_food(self):
        self.__chef.cook_burger()
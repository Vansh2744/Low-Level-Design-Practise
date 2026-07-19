from chef import Chef

class Waiter:
    def __init__(self, chef:Chef):
        self.__chef = chef

    def cook_food(self, food:str):
        if food == "burger":
            self.__chef.cook_burger()

        elif food == "pizza":
            self.__chef.cook_pizza()

        elif food == "french fries":
            self.__chef.cook_french_fries()
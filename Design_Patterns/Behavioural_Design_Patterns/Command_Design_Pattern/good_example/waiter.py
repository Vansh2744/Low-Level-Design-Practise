from command import Command

class Waiter:
    def give_food(self, food:Command):
        food.cook_food()


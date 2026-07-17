from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self, strategy: DiscountStrategy):
        self.__strategy = strategy

    def change_strategy(self, new_strategy: DiscountStrategy):
        self.__strategy = new_strategy

    def process_discount(self):
        self.__strategy.calculate_discount()
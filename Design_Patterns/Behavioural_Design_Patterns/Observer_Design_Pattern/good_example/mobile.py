from observer import Observer

class MobileDisplay(Observer):
    def __init__(self):
        self.__temp = 0

    def update_temp(self, temp):
        self.__temp = temp
        self.display_temp()

    def display_temp(self):
        print(f"Mobile Display Temperature = {self.__temp}")
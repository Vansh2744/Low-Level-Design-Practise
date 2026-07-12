from observer import Observer

class TVDisplay(Observer):
    def __init__(self):
        self.__temp = 0

    def update_temp(self, temp):
        self.__temp = temp
        self.display_temp()

    def display_temp(self):
        print(f"TV Display Temperature = {self.__temp}")
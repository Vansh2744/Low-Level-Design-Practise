class WeatherStation:
    def __init__(self):
        self.__temp = 0
        self.__tv_display = TVDisplay()
        self.__mobile_display = MobileDisplay()

    def update_temp(self, temp):
        self.__temp = temp
        self.notify_displays()

    def notify_displays(self):
        self.__tv_display.update_temp(self.__temp)
        self.__mobile_display.update_temp(self.__temp)



class TVDisplay:
    def __init__(self):
        self.__temp = 0

    def update_temp(self, temp):
        self.__temp = temp
        self.display_temp()
    
    def display_temp(self):
        print(f"TV Display Temperature = {self.__temp} Degrees")

class MobileDisplay:
    def __init__(self):
        self.__temp = 0

    def update_temp(self, temp):
        self.__temp = temp
        self.display_temp()
    
    def display_temp(self):
        print(f"Mobile Display Temperature = {self.__temp} Degrees")

ws = WeatherStation()
tv = TVDisplay()
mob = MobileDisplay()

ws.update_temp(34)
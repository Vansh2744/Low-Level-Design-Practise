from observer import Observer

class WeatherStation:
    def __init__(self):
        self.__temp = 0
        self.__observers = []

    def add_observer(self, obs:Observer):
        self.__observers.append(obs)

    def remove_observer(self, obs:Observer):
        self.__observers.remove(obs)

    def update_temp(self, temp):
        self.__temp = temp
        self.notify_observers()

    def notify_observers(self):
        for obs in self.__observers:
            obs.update_temp(self.__temp)
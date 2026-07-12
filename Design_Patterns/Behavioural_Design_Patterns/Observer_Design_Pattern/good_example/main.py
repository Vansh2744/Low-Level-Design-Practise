from weather_station import WeatherStation
from tv import TVDisplay
from mobile import MobileDisplay

ws = WeatherStation()
tv_dis = TVDisplay()
mob_dis = MobileDisplay()

ws.add_observer(tv_dis)
ws.add_observer(mob_dis)

ws.update_temp(34)
ws.remove_observer(tv_dis)
ws.update_temp(30)
from Weather import *
l = Weather.map_cityNum.keys()
print(Weather().getWeather())
for s in l :
    print(Weather(s).getWeather())
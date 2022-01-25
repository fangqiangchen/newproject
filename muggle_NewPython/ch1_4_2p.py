import urge

city1 = "mohe"
city2 = "guangzhou"

c1 = urge.get_simple_temp(city1).once()

c2 = urge.get_simple_temp(city2).once()

c3 = c2 - c1

print(c3)
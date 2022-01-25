import urge
import time

city = "beijing"
city1 = "nanjing"
lang = 'zh'

t1 = time.time()

result = urge.get_now_temp(city,lang).once()
result1 = urge.get_simple_temp(city1).once()
C = float(result1)
F = 32 + C * 1.8
f = round(F)
print(f)
t2 = time.time()
t = t2-t1
# print(result)
print(t)
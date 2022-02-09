import urge

temp = urge.get_now_temp("beijing").once()
print(temp)

if temp > 35:
    print("Today's hot")
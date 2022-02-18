import urge

temp = urge.get_now_temp("beijing").once()
print(temp)

if int(temp) > 35:
    print("Today's hot")
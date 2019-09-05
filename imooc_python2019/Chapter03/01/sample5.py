weight = int(input("请输入您的体重Kg："))
height = float(input("请输入您的身高:"))

bmi = weight / pow(height,2)
print(bmi)
if bmi  <= 18.4:
    print("测评结果：偏瘦")
elif bmi >18.4 and bmi <= 23.9:
    print("评测结果：正常")
elif bmi > 23.9 and bmi <= 27.9:
    print("评测结果：过重")
else:
    print("评测结果：肥胖")

has_ticket = input("乘客是否购买车票（1-是，0-否：")

knife_length = int(input("请输入刀具长度（公分，0-未携带"))

if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length < 20:
        print("道具为超过20厘米，允许上车")
    else:
        print("管制刀具，车站没收")
else:
    print("没有车票，不允许进站")
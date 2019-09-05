#break
#定义计数器
i = 0
while i < 3:
    mobile = input("请输入您要查询的手机号：")
    i += 1
    if mobile == "13312345678":
        print('您的花费余额为158元')
        break
print('感谢您的来电')

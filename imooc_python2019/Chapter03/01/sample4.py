high = input("请输入您测量的高压值：")
low = input("请输入您测量的低压值：")

high =int(high)
low = int(low)

# if (low >60 and low <90) and (high > 90 and high < 140):
#     print("您的血压正常，请继续保持健康的生活习惯")
# else:
#     print("您的血压出现异常，请尽快就医")

if (low <= 60 or low >=90) or (high >=140 or high <= 90):
    print("您的血压出现异常，请尽快就医")
else:
    print("您的血压正常，请继续保持健康的生活习惯")
print('欢迎使用阶梯电价计算器')

elec_num = 876

charge = (240 * 0.4883) + (400-240) * 0.5383 + (elec_num - 400) * 0.7883

print('您本月的用电量为：')
print(elec_num)
print('您本月的电价为')
print(charge)
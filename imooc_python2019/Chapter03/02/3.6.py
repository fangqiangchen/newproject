#求偶数之和
sum1 = 0
num1 = 1
while num1 < 1000:
    if num1%2 == 0:
        sum1 += num1
    num1+=1
print("1-1000之间偶数之和{0}".format(sum1))


#求奇数之和
sum1 = 0
num1 = 1
while num1 < 1000:
    if num1%2 == 1:
        sum1 += num1
    num1+=1
print("1-1000之间偶数之和{0}".format(sum1))
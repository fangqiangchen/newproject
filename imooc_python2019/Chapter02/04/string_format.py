name = "小明"
age = 25
height = 180.5
str1 = "我叫" + name + ",今年" + str(age) + "岁，身高" + str(height)
print(str1)
str2 = "我叫{},今年{},身高{}".format(name,age,height)
print(str2)
str3 = "我叫{0},身高{2},今年{1}".format(name,age,height)
print(str3)
#通过别名选择
str4 = "我叫{p1},我在{p2}班,身高{p4},今年{p3}".format(p1=name,p3=age,p4=height,p2='3-2')
print(str4)
#数字格式化输出
num = 1234567.89555
str4=format(num,'0.4f')
print(type(str4))
print(str4)

account = '8810381'
amt = 123456789
str5=format(amt,',')
print(str5)
str6=format(amt,'0,.2f')
print(str6)
str7 = '请您向{}账户转账¥{:0.3f}'.format(account,amt)
print(str7)
#早期单位字符串格式化
name = "张三"
age = 30
weight = 87.5
str8 = "我叫%s,今年%d,体重%.2f公斤"%(name,age,weight)
print(str8)
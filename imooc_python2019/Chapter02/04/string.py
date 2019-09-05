str1 = "hello world!"

str2 = 'Nice to meet you'

str3 = "I told my friend 'she is beautiful'"

str4 = "my dog's name is andy"

str5 = str1 + str2
print(str5)
#制表符与换行符
table = '姓名\t性别\t年龄\n赵四\t男士\t42'
print(table)
#删除空白
space_str = "   hello world    "
print(space_str)
lstr = len(space_str)
print(lstr)
nospace_str = space_str.strip()
print(nospace_str)
print(len(nospace_str))

#字符串查找
source = "Nice to meet you, i need your help"

index = source.find("ee", 17,22)
print(index)

isexist="ee" in source
print(isexist)
#字符串替换
str8 = 'this is string example...wow!!! this is really string'
pstr8 = str8.replace('is','was')
print(pstr8)
pstr8 = str8.replace('is','was',3)
print(pstr8)

text = "sunny"
print(text.replace('a','b'))
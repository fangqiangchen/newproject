year = int(input("请输入年份："))
if year/4 == 0:
    print("{0}年时闰年".format(year))
else:
    print("{0}年不是闰年".format(year))
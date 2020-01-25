books = ["三国演义","水浒传","红楼梦","西游记","镜花缘","封神演义","聊斋志异"]

for book in books:
    if book != "镜花缘":
        print(book)


for i in range(10,15):
    print(i)

for n in range(1,1000):

    i = n / 100
    i = int(i)

    j = n/10%10
    j = int(j)
    k = n %10
    result = i*i*i+j*j*j+k*k*k
    if n == result:
        print(n,end="")
        print("是水仙花数")


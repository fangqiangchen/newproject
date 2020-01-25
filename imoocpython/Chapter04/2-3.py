n = 100

while n < 1000:

    i = n / 100
    i = int(i)

    j = n/10%10
    j = int(j)
    k = n %10
    result = i*i*i+j*j*j+k*k*k
    if n == result:
        print(n,end="")
        print("是水仙花数")

    n = n +1
num = 1
count = 0
while num <= 100:
    if num % 3 == 0 or num % 7 == 0 and (num % 21 != 0):
        count+=1
    num+=1
print(count)
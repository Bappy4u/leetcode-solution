num = 512
rem = 0
res = 0
while num!=0:
    rem = num%10
    res = res * 10 + rem
    num = num // 10

print(res)

    
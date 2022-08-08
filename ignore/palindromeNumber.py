num = int(input())
n = num
temp = 0

while num !=0:
    rem = num%10
    temp = temp * 10 + rem

    num //=10

print("Yes") if n==temp else print("No")


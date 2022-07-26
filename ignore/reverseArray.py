ar = [1,2,3,4,5,6]

i = 0

while i<len(ar)//2:
    ar[i], ar[-1-i] = ar[-1-i], ar[i]
    i +=1

print(ar)

x = []
for i in range(len(ar)-1, -1, -1):
    x.append(ar[i])

x[::]=x[::-1]
print(x)
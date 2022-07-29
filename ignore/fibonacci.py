ar = []

ar.append(0)
ar.append(1)

for i in range(2, 10):
    ar.append(ar[i-1] + ar[i-2])


print(ar)

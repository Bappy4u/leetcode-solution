ar = [1,1,2,3,4,6,6]
max, min = max(ar), min(ar)

sum = sum(ar) - max -min
print(sum)
sum = 0
for n in ar:
    if n<min:
        min = n
    if n>max:
        max = n
    sum += n

sum -= min + max

print(sum)

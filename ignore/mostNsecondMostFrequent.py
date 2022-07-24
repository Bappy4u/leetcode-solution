message = "hello world"
d = {}
letters = set(message)
for l in message:
    d[message.count(l)] = l

print(d)
ar = sorted(d, reverse=True)

print(ar)
for i in range(2):
    print(d[ar[i]])
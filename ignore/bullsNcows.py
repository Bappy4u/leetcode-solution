a = input()
b = input()

bulls = 0
cows = 0
dic = {}
for i in range(len(a)):
    if a[i]==b[i]:
        bulls +=1

    if dic.get(a[i]):
        dic[a[i]] +=1
    else:
        dic[a[i]]=1
    if dic.get(b[i]):
        dic[b[i]] +=1
    else:
        dic[b[i]]=1


for d in dic:
    if dic[d]==2:
        cows +=1


print(f"{bulls} {cows-bulls}")
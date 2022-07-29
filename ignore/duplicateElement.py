nums = [1,2,3,3,3,4,4,5,]
res = {}
dic = {}

for n in nums:
    if dic.get(n):
        res[n] = None
    
    else:
        dic[n]= True

ar = list(res)
print(ar)

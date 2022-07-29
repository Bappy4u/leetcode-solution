nums = [1,1,2,2,3,3,4]
dic = {}
for n in nums:
    if dic.get(n):
        dic[n] +=1
    else:
        dic[n] = 1


for num in dic:
    
    if dic[num] == 1:
        print(num)

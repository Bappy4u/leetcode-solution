graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj"]
graph["alice"] = []
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = ["bappy"]
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = ["najmul"]
graph["najmul"]= ["bappy"]
graph["bappy"] = ["peggy"]

shortpath = 0
q= []
res = []
q.append(graph["you"])
count = 0
flag = 0
while q:
    neigbours = q.pop(0)
    temp = []
    if neigbours:
        count +=1
        for n in neigbours:
            if n=="bappy":
                print(f"found at {count} steps")
                res.append(count)
                flag = 1
                
            temp += graph[n]
        if temp:
            q.append(temp)
    

if flag:
    print(f"Shortest path to peggy is {min(res)}")

else:
    print("peggy not found")





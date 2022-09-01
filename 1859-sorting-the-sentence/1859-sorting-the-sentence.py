class Solution:
    def sortSentence(self, s: str) -> str:
        list = s.split(" ")
        
        res = [None for i in range(len(list))]
        
        for st in list:
            res[int(st[-1])-1]= st[:-1:]
            
        
        
        return " ".join(res)
        
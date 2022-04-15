class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        dic1 = {}
        dic2 = {}
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in dic1:
                dic1[ransomNote[i]] +=1
            else:
                dic1[ransomNote[i]] = 1
                
        for i in range(len(magazine)):        
            if magazine[i] in dic2:
                dic2[magazine[i]] +=1
            else:
                dic2[magazine[i]] = 1
                
                
        for v in dic1:

            if v not in dic2 or dic1[v]>dic2[v]:
                return False
            
        return True
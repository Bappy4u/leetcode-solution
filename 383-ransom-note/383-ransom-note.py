class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = {key: 0 for key in ransomNote}
        dic2 = {key: 0 for key in magazine}
 
        for key in ransomNote:
            dic1[key] +=1
            
        for key in magazine:
            dic2[key] +=1
            
        
        for key in dic1:
            if not dic2.get(key) or dic2[key]<dic1[key]:
                return False
            
        
        return True
        
        
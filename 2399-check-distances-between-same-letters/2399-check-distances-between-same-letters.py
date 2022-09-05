class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        visited = set()
        
        for k in range(len(s)-1):
            
            if s[k] in visited:
                continue;
            visited.add(s[k])
            for i in range(k+1, len(s)):
                
                if s[k]==s[i]:
                    if not i- k-1 == distance[ord(s[k])-97]:
                        
                        return False
                    else:
                        break
                    
            
        return True
        
def reverseword(s) -> str:
    left, right = 0, len(s)-1
        
    while left<right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    return "".join(s)

class Solution:
    def reverseWords(self, s: str) -> str:
        ars = s.split()
        res = []
        for w in ars:
  
            res.append(reverseword(list(w)))

        return " ".join(res)
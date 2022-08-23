class Solution:
    def reverseWords(self, s: str) -> str:
        ra = []
        i = 0
        while i<len(s):
            temp =""
            while i in range(len(s)) and s[i]!=" ":
                temp +=s[i]
                i +=1
            i +=1
            if temp:
                ra.append(temp)
        
        ns = " ".join(ra[::-1])
        return ns.strip()
        
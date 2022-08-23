class Solution:
    def reverseWords(self, s: str) -> str:
        ar = s.split(" ")
        ra = []
        
        for char in ar:
            if char:
                ra.append(char)
        ns = " ".join(ra[::-1])
        return ns.strip()
        
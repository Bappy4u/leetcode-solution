class Solution:
    def reverseWords(self, s: str) -> str:
        ra = [word for word in s.split(' ') if word]
        
        ns = " ".join(ra[::-1])
        return ns.strip()
        
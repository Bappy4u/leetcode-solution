class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            temp = sentence.split(" ")
            res = max(res, len(temp))
            
            
        
        return res
        
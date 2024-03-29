class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        
        for w in accounts:
            res = max(res, sum(w))
            
        return res
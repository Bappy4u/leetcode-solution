class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sol_count = []
        for i,val in enumerate(mat):
            sol_count.append([sum(val),i])
         
        sol_count.sort()
        
        res = []
        for i in range(k):
            res.append(sol_count[i][1])
        
        return res
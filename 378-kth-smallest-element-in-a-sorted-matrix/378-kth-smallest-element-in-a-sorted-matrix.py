class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        ar = []
        for array in matrix:
            ar +=array
            
        ar.sort()
        
        return ar[k-1]
            
        
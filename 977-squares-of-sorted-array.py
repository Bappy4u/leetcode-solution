class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res =  [0] * (r+1) 
        i = r
        while i>-1:
            
            if abs(nums[r])<abs(nums[l]):
                res[i]=nums[l]**2
                l +=1
            else:
                res[i]=nums[r]**2
                r -=1
                
            i -=1
            
 
        return res
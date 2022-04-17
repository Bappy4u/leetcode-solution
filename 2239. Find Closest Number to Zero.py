class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        res = []
        for n in nums:
            if n<0:
                res.append(n*-1)
            else:
                res.append(n)
                
        res.sort()
       
        for i in res:
            
            if i in nums:

                return i
            elif -i in nums:
                return -i
            
        
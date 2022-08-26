class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        tres = 0
        res = 0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]!=nums[i+1]-1:
                res = max(res,tres)
                tres = 0
            else:
                tres +=1
                
        res = max(res,tres)    

        return res+1

        
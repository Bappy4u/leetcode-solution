class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        nums.sort()
        temp=0
        print(nums)
        tres = 0
        res = 0
        for i in range(len(nums)-1):
            
            if nums[i]==nums[i+1]:
                temp +=1
            elif nums[i]!=nums[i+1]-1:
                res = max(res,tres)
                tres = 0
            else:
                tres +=1
                
        res = max(res,tres)    

        return res+1

        
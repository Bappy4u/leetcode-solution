class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                nums = nums[i:]
                break
        
        for i in range(len(nums)):
            if i+1 !=nums[i]:
                return i+1
            
        return i+2
        
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        ans = 0
        diff = float("inf")
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            anchor = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = anchor + nums[left] + nums[right]
                if abs(temp - target) < diff:
                    diff = abs(temp - target)
                    ans = temp        
                if temp > target:
                    right -= 1
                else:
                    left += 1
        return ans
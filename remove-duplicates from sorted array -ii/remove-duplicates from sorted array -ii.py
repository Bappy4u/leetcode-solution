from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        p1 = 2
        for i in range(2, len(nums)):
            if nums[p1 - 1] != nums[i]:
                nums[p1] = nums[i]
                p1 += 1
            elif nums[p1 - 1] == nums[i] and nums[p1 - 2] != nums[i]:
                nums[p1] = nums[i]
                p1 += 1

        return p1

sol = Solution()

print(sol.removeDuplicates([1,1,1,2,2,3]))
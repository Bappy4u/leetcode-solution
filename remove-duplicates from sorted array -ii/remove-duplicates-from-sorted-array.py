class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[p1] = nums[i]
                p1 += 1

        return p1

    dataset = [1, 2, 3]


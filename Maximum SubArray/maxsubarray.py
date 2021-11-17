from typing import List


def maxSubArray(nums: List[int]) -> int:
    contSum = nums[0]
    currSum = nums[0]
    for i in range(1, len(nums)):
        contSum = max(contSum, currSum)
        if currSum < 0:
            currSum = 0
        currSum += nums[i]
    return max(contSum, currSum)


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
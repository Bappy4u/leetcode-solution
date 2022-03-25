class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        r = goal
        while r>-1:
            if r + nums[r]>=goal:
                goal=r
            r -= 1
            
        return goal==0
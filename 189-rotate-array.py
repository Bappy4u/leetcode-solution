class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if not k==0:    
            nums1 = nums[-k:] + nums[:len(nums)-k]
            nums.clear()
            nums.extend(nums1)
def bsearch(nums, target):
    l, r = 0,len(nums)-1
    
    while l<=r:
        mid = (l+r)//2
        
        if nums[mid]==target:
            return True
        elif nums[mid]<target:
            l =mid+1
        else:
            r = mid-1
    
    return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        flag = 0
        for i,v in enumerate(nums):
            if i>0 and nums[i-1]>v:
                flag = 1
                break
        
        
        nums = nums[i:] + nums[:i] if flag else nums
        
        print(nums)
        
        return bsearch(nums, target)
        
    """
    One line soultion is:
    return targin in nums
    """
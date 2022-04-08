class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)-1
        
        while l<=r:
            mid = (r+l)//2
            if nums[mid]==target:
                l, r = mid-1, mid+1
                print(l)
                while (r<len(nums) and nums[r]==target) or (l>=0 and nums[l]==target):
                    if nums[r]==target:
                        r +=1
                    
                    if l>=0 and nums[l]==target:
                        l -=1
                
                return  [l+1, r-1]
            
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
                
                
        return [-1,-1]
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l, r= i+1, len(nums)-1
            
            while l<r:
                sum = nums[i] + nums [l] + nums[r]
                if sum<0:
                    l +=1
                elif sum>0:
                    r -=1
                else:
                    if [nums[i], nums [l], nums[r]] not in res:
                        res.append([nums[i], nums [l], nums[r]])
                    l +=1    
                    r -=1
        
        return res
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dic = {}
    
        for i in range(len(nums)-1):

            print(nums[i]+nums[i+1])
            if dic.get(nums[i]+nums[i+1]):

                return True
            else:
                dic[nums[i]+nums[i+1]]=1

        return False
        
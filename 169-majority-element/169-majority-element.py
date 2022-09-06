class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            if dic.get(n):
                dic[n] +=1
            else:
                dic[n] = 1
                
        res = []
        
        for n in dic:
            if dic[n]>len(nums)//2:
                return n
                

        
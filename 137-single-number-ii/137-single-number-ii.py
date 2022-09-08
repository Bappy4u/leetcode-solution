class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {key:0 for key in nums}
        
        for n in nums:
            dic[n] +=1
            
            
        for k in dic:
            if dic[k] == 1:
                return k
        
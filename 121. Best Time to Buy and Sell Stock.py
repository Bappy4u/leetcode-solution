class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxs = 0
        buy = 0
        sell = 1
        
        while sell<len(prices) and buy<len(prices)-1:
            if prices[buy]>prices[sell]:
                buy +=1
                sell =buy+1
            else:
                maxs = max(maxs, prices[sell]-prices[buy])
                sell +=1  
                
        return maxs
                
            
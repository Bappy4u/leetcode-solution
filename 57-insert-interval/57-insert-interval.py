class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        i = 0
        
        while i<len(intervals):
            
            if res and res[-1][1]>=intervals[i][0]:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
        
            else:
                res.append(intervals[i])
            i +=1
            
        return res
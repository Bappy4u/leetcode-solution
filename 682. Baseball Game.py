class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        total = 0
        for o in ops:
            if o=='C':
                temp = scores.pop()
                total -=temp
            elif o=='D':
                temp = scores[-1]*2
                total +=temp
                scores.append(temp)
            elif o=='+':
                temp = scores[-1]+scores[-2]
                total +=temp
                scores.append(temp)
            else:
                temp = int(o)
                scores.append(temp)
                total +=temp
        
        return total
        
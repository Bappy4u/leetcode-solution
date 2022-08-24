class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def three(n):
            
            if n==1:
                return True
            elif n and n%3==0:
                return three(n//3)
            else:
                return False
            
        
        return three(n)
        
        
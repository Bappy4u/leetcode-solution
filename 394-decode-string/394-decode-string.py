class Solution:
    def decodeString(self, s: str) -> str:
        digit = []
        
        stack = []
        res = ""
        i=0
        while i<len(s):
            if s[i].isdigit():
                d = 0
                while s[i].isdigit():
                    d = d*10 + int(s[i])
                    i +=1
                digit.append(d)    
            elif s[i]==']':
                x = digit.pop()
                temp =""
                while True:
                    y = stack.pop()
                    if y=="[":
                        break
                    temp = y + temp
                  
                stack.append(temp*x)
                
                i +=1
            else:
                stack.append(s[i])
                i +=1
                
        return "".join(stack)
class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        goal = {
            "()":'o',
            "(al)":'al',
            "G": 'G'
        }
        res = ""
        i=0
        while i<len(command):
            s=""
            while True:
                s +=command[i]
                i +=1
                if goal.get(s):
                    res += goal.get(s)
                    break
        
        return res
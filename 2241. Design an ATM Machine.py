class ATM:

    def __init__(self):
        self.note = {
            '4': 500,
            '3': 200,
            '2': 100,
            '1': 50,
            '0': 20,
        }
        self.noteCount = [0,0,0,0,0]
        self.balance = 0 

    def deposit(self, banknotesCount: List[int]) -> None:
        
        for i,v in enumerate(banknotesCount):
            self.noteCount[i] +=v
        
        
       
    def withdraw(self, amount: int) -> List[int]:
        res = []
        
        for i,n in enumerate(self.note):
           
            temp = amount//self.note[n]
            
            if temp >0:
                if self.noteCount[4-i]>=1:
                    if self.noteCount[4-i]<temp:
                        temp = self.noteCount[4-i]
                    amount -= self.note[n] * temp
                    res.append(temp)
                else:
                    res.append(0)
                    
            else:
                res.append(0)
                    
        
        res.reverse()
        if amount !=0:
            return [-1]

        else:
            for i in range(len(res)):
                self.noteCount[i] -= res[i]

            return res
                    
        

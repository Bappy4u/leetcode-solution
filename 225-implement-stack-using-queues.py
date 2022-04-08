class MyStack:
    
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            temp = self.queue.pop()
            
        return temp
        

    def top(self) -> int:
        if self.queue:
            return self.queue[-1]
        

    def empty(self) -> bool:
        return not self.queue
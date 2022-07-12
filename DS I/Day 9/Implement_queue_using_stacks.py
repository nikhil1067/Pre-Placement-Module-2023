class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        # We will push new elemts to stack1. 
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        
        # We will always pop from stack2 if any element is present. If not move all elements from stack1 to 2 and then pop the topmost. 
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self) -> int:
        if self.empty():
            return -1
        
        if self.stack2:
            return self.stack2[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
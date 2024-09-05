class MyQueue:

    def __init__(self):
        self.myqueue = []
        

    def push(self, x: int) -> None:
        self.myqueue.append(x)
        

    def pop(self) -> int:
        if self.myqueue:
            return self.myqueue.pop(0)
        

    def peek(self) -> int:
        if self.myqueue:
            return self.myqueue[0]
        

    def empty(self) -> bool:
        if self.myqueue:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
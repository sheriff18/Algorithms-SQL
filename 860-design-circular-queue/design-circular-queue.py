from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.popleft()
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]
        
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        
    def isFull(self) -> bool:
        return len(self.queue) == self.k

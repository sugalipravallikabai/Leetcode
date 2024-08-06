class MyQueue:

    def __init__(self):
        self.q = [0]*100000
        self.st = 0
        self.end = 0

    def push(self, x: int) -> None:
        self.q[self.end] = x
        self.end += 1

    def pop(self) -> int:
        if self.st == self.end:
            return self.q[self.st]
        temp = self.st
        self.st += 1
        return self.q[temp]
        

    def peek(self) -> int:
        if self.st == self.end:
            return self.q[self.st]
        return self.q[self.st]

    def empty(self) -> bool:
        if self.st == self.end:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
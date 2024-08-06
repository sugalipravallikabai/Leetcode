class MyStack:

    def __init__(self):
        self.q = [0]*100000
        self.ptr = 0

    def push(self, x: int) -> None:
        self.q[self.ptr] = x
        self.ptr += 1

    def pop(self) -> int:
        if self.ptr == 0:
            return self.q[self.ptr]
        temp = self.ptr-1
        self.ptr -= 1
        return self.q[temp]
        
    def top(self) -> int:
        if self.ptr == 0:
            return self.q[self.ptr]
        temp = self.ptr-1
        # self.ptr -= 1
        return self.q[temp]

    def empty(self) -> bool:
        
        if self.ptr == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.st = []
        self.topind = 0

    def push(self, val: int) -> None:
        self.st.append(val)
        self.topind += 1

    def pop(self) -> None:
        if self.topind == 0:
            return None
        self.topind -= 1
        return self.st.pop()

    def top(self) -> int:
        if self.topind == 0:
            return None
        return self.st[self.topind - 1]

    def getMin(self) -> int:
        if self.topind == 0:
            return None  
        mini = float('inf')
        for i in range(self.topind):
            mini = min(self.st[i], mini)
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
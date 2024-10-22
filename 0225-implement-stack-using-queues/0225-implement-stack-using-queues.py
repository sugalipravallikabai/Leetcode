class MyStack:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        if self.st:
            return self.st.pop()
        return -1

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def empty(self) -> bool:
        return True if len(self.st) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0
        
    def insert(self, idd : int, val : str) -> List[str]:
        
        idd -= 1
        self.data[idd] = val
        if self.ptr < idd : return []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr+=1
        return self.data[idd:self.ptr]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
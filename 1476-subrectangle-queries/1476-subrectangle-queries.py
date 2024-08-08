class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.r = rectangle
        

    def updateSubrectangle(self, r1: int, c1: int, r2: int, c2: int, val : int) -> None:
        
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                self.r[i][j] = val
        return self.r

    def getValue(self, row: int, col: int) -> int:
        
        val = self.r[row][col]
        
        return val


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
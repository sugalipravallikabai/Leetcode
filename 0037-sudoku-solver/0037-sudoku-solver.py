class Solution:
    def solveSudoku(self, b : List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def possible(b,r,c,n):
            for i in range(9):
                if b[r][i] == n:
                    return False
            for j in range(9):
                if b[j][c] == n:
                    return False
            
            x0 = (r//3)*3
            y0 = (c//3)*3
            
            for i in range(3):
                for j in range(3):
                    if b[x0+i][y0+j] == n:
                        return False
            return True
            
            
        def solve(b):
            
            for x in range(9):
                for y in range(9):
                    if b[x][y] == '.':
                        for n in map(str,range(1,10)):
                            if possible(b,x,y,n):
                                b[x][y] = n
                                if solve(b):
                                    return True
                                b[x][y] = '.'
                        return False
            return True
        solve(b)
        # return b
                            
        
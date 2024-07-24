class Solution:
    def rotate(self, m : List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(m),len(m[0])
        res = [[0]*r for _ in range(c)]
        
        for i in range(r):
            for j in range(c):
                
                res[j][r-1-i] = m[i][j]
                
        for i in range(r):
            for j in range(c):
                
                m[i][j] = res[i][j]
                
        return m
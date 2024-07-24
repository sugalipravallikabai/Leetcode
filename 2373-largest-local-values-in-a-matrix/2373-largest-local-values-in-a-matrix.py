class Solution:
    def largestLocal(self, g : List[List[int]]) -> List[List[int]]:
        
        r,c = len(g),len(g[0])
        res = [[0] * (c-2) for _ in range(r-2)]
        
        def maxi(row,col):
            best = g[row][col]
            
            for i in range(row,row+3):
                for j in range(col,col+3):
                    
                    best = max(g[i][j],best)
            return best
        
        for i in range(c-2):
            for j in range(r-2):
                
                res[i][j] = maxi(i,j)
        return res
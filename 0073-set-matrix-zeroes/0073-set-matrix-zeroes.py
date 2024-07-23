class Solution:
    def setZeroes(self, m : List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r,c = len(m),len(m[0])
        c1 = 0
        for i in range(r):
            for j in range(c):
                
                if m[i][j] == 0:
                    
                    m[i][0] = 0
                    
                    if j == 0:
                        
                        c1 = 1
                    
                    else:
                        m[0][j] = 0
        
        for i in range(1,r):
            for j in range(1,c):
                if m[i][j] != 0:
                    if m[i][0] == 0 or m[0][j]  == 0:
                        m[i][j] = 0
        
        if m[0][0] == 0:
            for j in range(c):
                
                m[0][j] = 0
        if c1 == 1:
            for i in range(r):
                m[i][0] = 0
        
        return m
            
        
                
                    
                    
        
class Solution:
    def setZeroes(self, m : List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r,c = len(m),len(m[0])
        
        t1 = [0] * r
        t2 = [0] * c
        
        for i in range(r):
            for j in range(c):
                
                if m[i][j] == 0:
                    
                    t1[i] = 1
                    t2[j] = 1
                    
        for i in range(r):
            for j in range(c):
                
                if t1[i] == 1 or t2[j] == 1:
                    
                    m[i][j] = 0
        return m
                    
                    
        
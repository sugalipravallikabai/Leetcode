class Solution:
    def rotate(self, m : List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        
        for i in range(n):
            for j in range(i,n):
                
                m[i][j] , m[j][i] = m[j][i] , m[i][j]
                
        for i in range(n):
            m[i].reverse()
        
        return m
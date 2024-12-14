class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def fun(i,j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0 : 
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            left = fun(i,j-1)
            up = fun(i-1,j)
            dp[i][j]= left+up
            return dp[i][j]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        return fun(n-1,m-1)
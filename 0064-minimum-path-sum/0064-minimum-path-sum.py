class Solution:
    def minPathSum(self, g : List[List[int]]) -> int:
        n,m = len(g),len(g[0])
        def fun(i,j):
            if i == 0 and j == 0:
                return g[0][0]
            if i < 0 or j < 0 : 
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            left = g[i][j]+fun(i,j-1)
            up = g[i][j]+fun(i-1,j)
            dp[i][j]= min(left,up)
            return dp[i][j]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        return fun(n-1,m-1)
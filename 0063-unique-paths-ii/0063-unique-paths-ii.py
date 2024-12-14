class Solution:
    def uniquePathsWithObstacles(self, ob : List[List[int]]) -> int:
        n,m = len(ob),len(ob[0])
        mod = 2*(10**9)
        if ob[0][0] == 1 or ob[n-1][m-1] == 1:
            return 0
        def fun(i,j,dp):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if ob[i][j] == 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            left = fun(i,j-1,dp)
            up = fun(i-1,j,dp)
            dp[i][j] = left+up
            return dp[i][j]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return fun(n-1,m-1,dp)
        
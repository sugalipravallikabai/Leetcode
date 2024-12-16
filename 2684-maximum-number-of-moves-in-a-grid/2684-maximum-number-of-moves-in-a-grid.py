class Solution:
    def maxMoves(self, g : List[List[int]]) -> int:
        n,m = len(g),len(g[0])
        dp = [[-1] * m for _ in range(n)]
        def fun(i,j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            maxi = 0
            d = [(0, 1), (-1, 1), (1, 1)]
            for x,y in d:
                ni,nj = x+i,y+j
                if (ni >= 0 and ni < n) and (nj >= 0 and nj < m) and g[i][j] < g[ni][nj]:
                    maxi = max(maxi,1+fun(ni,nj))
            dp[i][j] = maxi
            return dp[i][j]
        result = 0
        for i in range(n):
            result = max(result,fun(i,0))
        return result
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n,m = len(w1),len(w2)
        dp = [[0 for _ in range(m)]for _ in range(n)]
        
        def fun(i,j):
            if i < 0 :
                return j+1
            if j < 0:
                return i+1
            if dp[i][j] != 0:
                return dp[i][j]
            if w1[i] == w2[j]:
                dp[i][j] = fun(i-1,j-1)
                return dp[i][j]
            dp[i][j] = 1+min(fun(i-1,j),fun(i,j-1),fun(i-1,j-1))
            return dp[i][j]
        return fun(n-1,m-1)
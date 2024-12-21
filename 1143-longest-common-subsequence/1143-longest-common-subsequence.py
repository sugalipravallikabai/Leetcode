class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dp = [[-1 for _ in range(m)]for _ in range(n)]
        def fun(i,j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1+fun(i-1,j-1)
                return dp[i][j]
            dp[i][j] = max(fun(i-1,j),fun(i,j-1))
            return dp[i][j]
        ans = fun(n-1,m-1)
        return 0 if ans == -1 else ans
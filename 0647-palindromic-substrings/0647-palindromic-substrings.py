class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = m = len(s)
        dp = [[False for _ in range(m+1)]for _ in range(n+1)]
        for i in range(n):
            dp[i][i] = True
            cnt += 1
        for i in range(2,n+1):
            for j in range(m-i+1):
                length = i+j-1
                if s[j] == s[length]:
                    if i == 2 or dp[j+1][length-1]:
                        cnt += 1
                        dp[j][length] = True
        return cnt
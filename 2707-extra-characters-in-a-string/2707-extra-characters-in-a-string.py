class Solution:
    def minExtraChar(self, s: str, d : List[str]) -> int:
        
        n = len(s)
        dt = set(d)
        dp = [0] * (n+1)
        # print(dt)
        for i in range(n-1,-1,-1):
            dp[i] = 1+dp[i+1]
            for j in range(i,n):
                curr = s[i:j+1]
                if curr in dt:
                    dp[i] = min(dp[i],dp[j+1])
        
        return dp[0]
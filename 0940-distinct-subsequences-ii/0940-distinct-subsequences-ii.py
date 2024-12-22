class Solution:
    def distinctSubseqII(self, s: str) -> int:
        d = {}
        mod = (10**9)+7
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            char = s[i-1]
            dp[i] = (2*dp[i-1])%mod
            if char in d:
                dp[i] -= dp[d[char]-1]
            d[char] = i
        print(dp)
        return (dp[n]-1)%mod
  
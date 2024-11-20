class Solution:
    def maxRepeating(self, s: str, w: str) -> int:
        n = len(w)
        m = len(s)
        dp = [0]* (m+1)
        for i in range(n,m+1):
            if s[i-n:i] == w:
                dp[i] = dp[i-n] + 1
                
        return max(dp)
                
            

class Solution:
    def maxProfit(self, p : List[int]) -> int:
        
        mini = p[0]
        dp = [0]*(len(p))
        
        for i in range(1,len(p)):
            
            mini = min(mini,p[i])
            dp[i] = max(dp[i-1],p[i]-mini)
        return dp[-1]
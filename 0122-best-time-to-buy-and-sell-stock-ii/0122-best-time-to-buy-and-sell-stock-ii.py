class Solution:
    def maxProfit(self, p : List[int]) -> int:
        mini = 0
        dp = [0]*len(p)
        for i in range(1,len(p)):
            mini = min(p[i-1],p[i])
            dp[i] = p[i] - mini
            
        return sum(dp)
        
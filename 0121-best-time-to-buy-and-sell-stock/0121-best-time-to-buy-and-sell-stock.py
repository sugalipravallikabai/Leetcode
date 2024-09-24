class Solution:
    def maxProfit(self, p : List[int]) -> int:
        
        mini = p[0]
        profit = 0
        
        for i in range(1,len(p)):
            cost = p[i]-mini
            profit = max(cost,profit)
            mini = min(mini,p[i])
        return profit
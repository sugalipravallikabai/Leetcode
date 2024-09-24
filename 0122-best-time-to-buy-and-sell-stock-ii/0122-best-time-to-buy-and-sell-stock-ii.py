class Solution:
    def maxProfit(self, p : List[int]) -> int:
        mini = p[0]
        tol = 0
        for i in range(1,len(p)):
            mini = min(mini,p[i])
            x = p[i] - mini
            if x > 0:
                tol += x
            mini = p[i]
        return tol
        
class Solution:
    def maxProfit(self, p : List[int]) -> int:
        m = float('-inf')
        a = [0]*len(p)
        for i in range(len(p)-1,-1,-1):
            m = max(m,p[i])
            a[i] = m
        res = float('-inf')
        for j in range(len(p)):
            res = max(a[j] - p[j],res)
        return res
            
            
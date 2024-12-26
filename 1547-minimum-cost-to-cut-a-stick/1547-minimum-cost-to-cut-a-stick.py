class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        arr = [0]+cuts+[n]
        m = len(arr)
        dp = [[-1 for _ in range(m+1)]for _ in range(m+1)]
        def fun(i,j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            mini = float('inf')
            for ind in range(i,j+1):
                cost = arr[j+1] - arr[i-1]+fun(i,ind-1)+fun(ind+1,j)
                mini = min(mini,cost)
            dp[i][j] = mini
            return dp[i][j]
        return fun(1,m-2)
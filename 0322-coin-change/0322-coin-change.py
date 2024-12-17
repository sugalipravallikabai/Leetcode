class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)]for _ in range(n)]
        def fun(i,k):
            if i == 0:
                if k%coins[i]==0:
                    return k//coins[i]
                return float('inf')
            if dp[i][k] != -1:
                return dp[i][k]
            notpick = 0+fun(i-1,k)
            pick = float('inf')
            if coins[i] <= k:
                pick = 1+fun(i,k-coins[i])
            dp[i][k]= min(pick,notpick)
            return dp[i][k]
        ans = fun(n-1,amount)
        return -1 if ans == float('inf') else ans
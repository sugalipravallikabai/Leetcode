class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)]for _ in range(n)]
        def fun(i,k):
            if i == 0:
                if k%coins[i]==0:
                    return 1
                return 0
            if dp[i][k] != -1:
                return dp[i][k]
            notpick = fun(i-1,k)
            pick = 0
            if coins[i] <= k:
                pick = fun(i,k-coins[i])
            dp[i][k]= pick+notpick
            return dp[i][k]
        ans = fun(n-1,amount)
        return ans     
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = (sum(nums)-target)//2
        if (sum(nums) - target) < 0 or (sum(nums) - target) % 2 != 0:
            return 0

        dp = [[-1 for _ in range(k+1)]for _ in range(n)]
        def fun(i,k):
            if k < 0:
                return 0 
            if i == 0:
                if nums[i] == 0 and k == 0:
                    return 2
                if nums[i] == k or k == 0:
                    return 1
                return 0
            if dp[i][k] != -1:
                return dp[i][k]
            notpick = fun(i-1,k)
            pick = 0
            if nums[i] <= k:
                pick = fun(i-1,k-nums[i])
            dp[i][k] = pick+notpick
            return dp[i][k]
        return fun(n-1,k)
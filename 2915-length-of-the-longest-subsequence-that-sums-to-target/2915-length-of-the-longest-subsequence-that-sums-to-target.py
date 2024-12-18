class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        k = target
        dp = [[-1 for _ in range(k + 1)] for _ in range(n)]
        def fun(i, k):
            if k < 0:
                return float('-inf')
            if i == 0:
                if nums[i] == k:
                    return 1
                if k == 0:
                    return 0
                return float('-inf')
            if dp[i][k] != -1:
                return dp[i][k]
            notpick = 0+fun(i-1,k)
            pick = float('-inf')
            if nums[i] <= k:
                pick = 1+fun(i-1,k-nums[i])
            dp[i][k] = max(pick,notpick)
            return dp[i][k]
        ans = fun(n - 1, k)
        return ans if ans > 0 else -1

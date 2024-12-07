from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        tol = 0
        cnt = 0
        d = defaultdict(int)
        for i in range(n):
            tol += nums[i]
            if tol == goal:
                cnt += 1
            cnt += d[tol-goal]
            d[tol]+=1
        return cnt

        
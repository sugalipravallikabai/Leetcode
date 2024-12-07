class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        d = {}
        n,tol,cnt=len(nums),0,0
        for i in range(n):
            tol += nums[i]
            if tol == k:
                cnt += 1
            if tol - k in d:
                cnt += d[tol-k]
            if tol in d:
                d[tol] += 1
            else:
                d[tol] = 1
        return cnt
                
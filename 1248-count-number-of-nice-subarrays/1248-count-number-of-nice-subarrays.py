from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        a = [0]*n
        for i in range(n):
            if nums[i]%2 == 1:
                a[i] = 1
        d = defaultdict(int)
        d[0] = 1
        cnt = 0
        tol = 0
        for i in range(n):
            tol += a[i]
            cnt += d[tol-k]
            d[tol] += 1
        return cnt
        
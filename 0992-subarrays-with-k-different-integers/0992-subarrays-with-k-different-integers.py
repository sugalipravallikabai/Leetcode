from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def fun(goal):
            cnt = 0
            d = defaultdict(int)
            l,r = 0,0
            while r < n:
                d[nums[r]] += 1
                while len(d) >goal:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        del d[nums[l]]
                    l += 1
                if len(d) <= goal:
                    cnt += r-l
                r += 1
            return cnt
        return fun(k) - fun(k-1)
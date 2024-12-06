class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        l , r = 0,0
        m = 0
        n = len(nums)
        zeros = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k :
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                m = max(m,r-l+1)
            r += 1
        return m
                
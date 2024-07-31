class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tol = 0
        m = float('-inf')
        for i in range(len(nums)):
            tol += nums[i]
            if tol > m:
                m = tol
            if  tol < 0:
                tol = 0
        return m
          
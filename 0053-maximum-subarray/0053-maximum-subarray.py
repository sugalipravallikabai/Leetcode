class Solution:
    def maxSubArray(self, n : List[int]) -> int:
        
        tol = 0
        m = float('-inf')
        for i in range(len(n)):
            tol += n[i]
            if tol > m:
                m = tol
            if tol < 0:
                tol = 0
        return m
            
          
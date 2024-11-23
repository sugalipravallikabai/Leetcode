class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        
        if len(n) == 1:
            return n[0]
        m = float('-inf')
        l = r = 0
        tol = 0
        while r < len(n):
            while tol < 0 and l < r:
                tol -= n[l]
                l+=1
            tol += n[r]
            m = max(m,tol)
            r += 1
        
        return m
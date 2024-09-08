class Solution:
    def missingNumber(self, n : List[int]) -> int:
        m = len(n)
        tol = (m*(m+1))//2
        return tol - sum(n)
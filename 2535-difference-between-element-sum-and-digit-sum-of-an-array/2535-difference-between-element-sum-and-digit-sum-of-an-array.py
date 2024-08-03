class Solution:
    def differenceOfSum(self, n : List[int]) -> int:
        tol = sum(n)
        dtol = 0
        for i in range(len(n)):
            val = n[i]
            while val > 0:
                dtol += val%10
                val = val//10
        return abs(tol-dtol)
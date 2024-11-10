class Solution:
    def clumsy(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n==3:
            return 3*2
        if n==4:
            return 4*3//2+1
        
        res = n * (n-1) // (n-2) + (n-3)
        n -= 4
        
        while n >= 4:
            res -= n * (n-1) // (n-2)
            res += (n-3)
            n -= 4
        if n == 3:
            res -= 3*2//1
        elif n == 2:
            res -= 2*1
        elif n == 1:
            res -= 1
        
        return res
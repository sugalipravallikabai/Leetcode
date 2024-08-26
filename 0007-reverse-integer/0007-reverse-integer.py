class Solution:
    def reverse(self, x: int) -> int:
        rem = 0
        og = x
        x = abs(x)
        while  x > 0:
            temp = x % 10
            rem = rem * 10 + temp
            x = x // 10
        if og < 0:
            rem = -rem
        if rem < -2**31 or rem > 2**31-1:
            return 0
        return rem
        
            
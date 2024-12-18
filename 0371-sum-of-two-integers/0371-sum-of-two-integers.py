class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        mask_int = 0x7fffffff
        while b != 0:
            temp = (a^b)&mask
            b = ((a&b)<<1)&mask
            a = temp
        return a if a <= mask_int else ~(a^mask)
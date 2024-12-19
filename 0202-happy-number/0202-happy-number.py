class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(num):
            return sum(int(digit)**2 for digit in str(num))
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = fun(n)
            if n == 1:
                return True
        return n == 1
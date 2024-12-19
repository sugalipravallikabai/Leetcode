class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def fun(num):
            return sum(int(digit) for digit in str(num))
        if fun(n) <= target:
            return 0
        add = 1
        initial = n
        while fun(n) > target:
            n = ((n//10**add)+1) * (10**add)
            add += 1
        return n - initial
    

#         while self.get_sum(n) > target:
#             n = ((n // (10**x)) + 1) * (10**x)
#             x += 1
#         return n - init

#     def get_sum(self, n: int) -> int:
#         return sum([int(d) for d in str(n)])
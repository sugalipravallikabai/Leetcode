class Solution:
    def fib(self, n: int) -> int:
        if n <= 2:
            if n == 0:
                return 0
            return 1
        pre = 0
        pr1 = 1
        for i in range(n-1):
            cur = pre+pr1
            pre = pr1
            pr1 = cur
        return pr1
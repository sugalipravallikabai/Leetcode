class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        pre,pre1 = 0,1
        for i in range(2,n+1):
            cur = pre+pre1
            pre = pre1
            pre1 = cur
        return pre1
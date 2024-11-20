class Solution:
    def tribonacci(self, n: int) -> int:
        pre = 0
        pre1 = 1
        pre2 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        for i in range(3,n+1):
            cur = pre+pre1+pre2
            pre = pre1
            pre1 = pre2
            pre2 = cur
        return pre2
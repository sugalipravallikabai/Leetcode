class Solution:
    def climbStairs(self, n: int) -> int:
        pre1 = 1
        pre = 1
        for i in range(2,n+1):
            cur = pre + pre1
            pre = pre1
            pre1 = cur
        return pre1
class Solution:
    def rob(self, n : List[int]) -> int:
        if len(n) == 0:
            return 0 
        if len(n) == 1:
            return n[0]
        pre1 = n[0]
        pre2 = max(n[0],n[1])
        for i in range(2,len(n)):
            cur = max(pre1+n[i],pre2)
            pre1 = pre2
            pre2 = cur
        return pre2
class Solution:
    def rob(self, n : List[int]) -> int:
        if len(n) == 0 :
            return 0
        if len(n) == 1:
            return n[0]
        t1 = []
        t2 = []
        def fun(t):
            if len(t) == 1:
                return t[0]
            pre1 = t[0]
            pre2 = max(t[0],t[1])
            for i in range(2,len(t)):
                cur = max(pre1+t[i],pre2)
                pre1 = pre2
                pre2 = cur
            return pre2
            
        for i in range(len(n)):
            if i != 0:
                t1.append(n[i])
            if i != len(n)-1:
                t2.append(n[i])
        
        return max(fun(t1),fun(t2))
        
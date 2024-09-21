class Solution:
    def firstMissingPositive(self, n : List[int]) -> int:
        
        m = len(n)
        d = [False] * (m+1)
        
        for v in n:
            if 0 < v <= m:
                d[v] = True
        for i in range(1,m+1):
            if d[i] == False:
                return i
        return m+1
                
        
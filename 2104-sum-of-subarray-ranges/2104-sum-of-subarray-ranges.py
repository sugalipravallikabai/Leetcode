class Solution:
    def subArrayRanges(self, n : List[int]) -> int:
        
        tol = 0
        for i in range(len(n)):
            s = n[i]
            l = n[i]
            for j in range(i+1,len(n)):
                l = max(l,n[j])
                s = min(s,n[j])
                tol = tol+(l-s)
        return tol
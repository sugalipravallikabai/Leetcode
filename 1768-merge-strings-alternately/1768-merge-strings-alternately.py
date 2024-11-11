class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res = ''
        n,m = len(w1),len(w2)
        i,j = 0,0
        while i < n and j < m:
            res += w1[i]
            res += w2[j]
            i+=1
            j+=1
        if i < n:
            res += w1[i:]
        elif j < m:
            res += w2[j:]
        return res
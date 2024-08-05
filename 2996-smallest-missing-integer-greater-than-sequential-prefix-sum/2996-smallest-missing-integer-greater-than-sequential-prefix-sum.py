class Solution:
    def missingInteger(self, a : List[int]) -> int:
        
        n = len(a)
        i = 1
        s = set(a)
        t = a[0]
        while i < n and a[i] == a[i-1]+1:
            
            t += a[i]
            i += 1
        while t in s:
            t += 1
        return t
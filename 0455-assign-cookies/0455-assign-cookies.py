class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n,m = len(g),len(s)
        l,r = 0,0
        while l < n and r < m:
            if s[r] >= g[l]:
                l+=1
                r+=1
            else:
                r+=1
        return l
                
class Solution:
    def garbageCollection(self, g : List[str], t : List[int]) -> int:
        
        cg = 0
        cm = 0
        cp = 0
        ans = 0
        for i in range(len(g)):
            if 'G' in g[i]:
                cg = i
            if 'P' in g[i]:
                cp = i
            if 'M' in g[i]:
                cm = i
            ans += len(g[i])
        ans += sum(t[:cm])+sum(t[:cg])+sum(t[:cp])
        
        return ans
                
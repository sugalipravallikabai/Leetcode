class Solution:
    def minimumAverage(self, n : List[int]) -> float:
        
        n.sort()
        m = len(n)
        res = []
        for i in range(len(n)):
            s = n[i]
            l = n[m-i-1]
            ans = (s+l) / 2
            res.append(ans)
        res.sort()
        return res[0]
            
class Solution:
    def getLongestSubsequence(self, w : List[str], g : List[int]) -> List[str]:
        res = [w[0]]
        t = g[0]
        for i in range(1,len(w)):
            if t != g[i]:
                res.append(w[i])
                t = g[i]
        return res
        
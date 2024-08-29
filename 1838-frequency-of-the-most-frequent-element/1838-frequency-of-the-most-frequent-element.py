class Solution:
    def maxFrequency(self, n : List[int], k: int) -> int:
        n.sort()
        m = 1
        l,t = 0,0
        for r in range(len(n)):
            t += n[r]
            while n[r] * (r-l+1) > t+k:
                t -= n[l]
                l += 1
            m =max(m,r-l+1)
        return m
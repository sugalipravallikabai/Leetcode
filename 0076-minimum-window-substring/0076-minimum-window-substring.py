from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        d = defaultdict(int)
        st = -1
        cnt = 0
        minlen = float('inf')
        l,r = 0,0
        for i in range(m):
            d[t[i]] += 1
        while r < n:
            if d[s[r]] > 0:
                cnt += 1
            d[s[r]] -= 1
            while cnt == m:
                if r-l+1 < minlen:
                    minlen = r-l+1
                    st = l
                d[s[l]] += 1
                if d[s[l]] > 0:
                    cnt -= 1
                l+=1
            r += 1
        return '' if st == -1 else s[st:minlen+st]
        
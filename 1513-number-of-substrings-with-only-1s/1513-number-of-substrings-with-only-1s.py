class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        l = 0
        mod = (10**9)+7
        while l  < len(s):
            if s[l] == '1':
                r = l
                while r < len(s) and s[r] == '1':
                    r += 1
                size = r-l
                cnt += (size*(size+1))//2
                cnt %= mod
                l = r
            else:
                l += 1
        return cnt
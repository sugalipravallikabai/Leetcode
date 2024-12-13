class Solution:
    def numSub(self, s: str) -> int:
        l = 0
        cnt = 0
        mod = (10**9)+7
        while l < len(s):
            if s[l] == '1':
                r = l
                while r < len(s) and s[r] == '1':
                    r += 1
                leng = r-l
                cnt += (leng*(leng+1))//2
                cnt %= mod
                l = r
            else:
                l += 1
        return cnt
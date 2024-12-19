class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        cnt = 0
        zeros = s.count('0')
        ones = n-zeros
        zeroprefix = oneprefix = 0
        for c in s:
            if c == '0':
                cnt += oneprefix*(ones-oneprefix)
                zeroprefix += 1
            else:
                cnt += zeroprefix*(zeros-zeroprefix)
                oneprefix += 1
        return cnt
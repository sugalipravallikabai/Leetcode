import math
class Solution:
    def minimumMoves(self, s: str) -> int:
        if 'O' not in s:
            return math.ceil(len(s)/3)
        if 'X' not in s:
            return 0
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == 'X':
                ans += 1
                i +=  3
            else:
                i+=1
        return ans
            
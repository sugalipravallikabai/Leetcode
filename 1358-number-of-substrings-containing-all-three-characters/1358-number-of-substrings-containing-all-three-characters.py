class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s:
            return 0
        cnt  = 0
        n = len(s)
        seen = {'a':-1,'b':-1,'c':-1}
        for i in range(n):
            seen[s[i]] = i
            if seen['a'] != -1 and seen['b'] != -1 and seen['c'] != -1:
                cnt += min(seen['a'],seen['b'],seen['c'])+1
        return cnt
    
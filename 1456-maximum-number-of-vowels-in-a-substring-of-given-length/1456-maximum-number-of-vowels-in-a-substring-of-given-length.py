class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        cnt = 0
        v = 'aeiou'
        for i in range(k):
            if s[i] in v:
                cnt += 1
        maxi = cnt
        for i in range(k,n):
            if s[i] in v:
                cnt += 1
            if s[i-k] in v:
                cnt -= 1
            maxi = max(maxi,cnt)
        return maxi
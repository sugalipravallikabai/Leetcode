class Solution:
    def findUnsortedSubarray(self, n: List[int]) -> int:
        s = sorted(n)
        l,r = 0,len(n)-1
        if s == n or len(n)==1:
            return 0
        for i in range(len(n)):
            if n[l] == s[l]:
                l += 1
            if n[r] == s[r]:
                r -= 1
            if l == r:
                return 0
        return r-l+1
         
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        print(r)
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                print(i)
                return r[:i]+s
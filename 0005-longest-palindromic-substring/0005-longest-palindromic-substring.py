class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxi = 0
        t = ''
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                # print(s[j:i:-1])
                if s[i:j] == s[j:i:-1]:
                    if maxi < j-i+1:
                        maxi = j-i+1
                        t = s[i:j+1]
        return t
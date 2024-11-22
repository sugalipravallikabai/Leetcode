class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if len(sub) > len(ans):
                        ans = sub
        return ans
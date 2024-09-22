class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def fun(l,r,s):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]
        
        ans = ""
        odd = ""
        even = ""
        
        for i in range(len(s)):
            
            odd = fun(i,i,s)
            if len(odd) > len(ans):
                ans = odd
            
            even = fun(i,i+1,s)
            if len(even) > len(ans):
                ans = even
                
        return ans
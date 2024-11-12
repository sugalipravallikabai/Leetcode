class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        k = ''
        if len(s) > len(t):
            return False
        for c in t:
            if  i < len(s) and c == s[i]:
                k += c
                i+=1
            if i > len(s):
                break
            if k == t:
                return True
        print(k)
        return k == s
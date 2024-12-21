class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        l,r,res,ss= 0,len(s)-1,0,list(s)
        while l < r:
            if ss[l] != ss[r]:
                i = r
                while i > l and ss[l] != ss[i]:
                    i -= 1
                if i == l:
                    ss[i],ss[i+1] = ss[i+1],ss[i]
                    res += 1
                    continue
                else:
                    while i < r:
                        ss[i],ss[i+1] = ss[i+1],ss[i]
                        i+=1
                        res+=1
            l,r = l+1,r-1
        return res
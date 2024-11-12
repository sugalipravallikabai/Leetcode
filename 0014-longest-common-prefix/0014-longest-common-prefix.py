class Solution:
    def longestCommonPrefix(self, s : List[str]) -> str:
        
        s = sorted(s)
        print(s)
        x = s[0]
        y = s[-1]
        
        for i in range(min(len(x),len(y))):
            if x[i] != y[i]:
                return x[:i]
                break
        return x
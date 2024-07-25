class Solution:
    def mostWordsFound(self, s : List[str]) -> int:
        
        maxi = 0
        for i in s:
            m=i.count(' ')
            maxi = max(maxi,m+1)
        return maxi
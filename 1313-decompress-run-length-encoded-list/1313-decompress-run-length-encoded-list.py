class Solution:
    def decompressRLElist(self, n : List[int]) -> List[int]:
        
        res = []
        
        for i in range(0,len(n)-1,2):
            res += [n[i+1]]*n[i]
        return res
            
class Solution:
    def decompressRLElist(self, n : List[int]) -> List[int]:
        
        res = []
        
        for i in range(0,len(n)-1,2):
            for j in range(n[i]):
                res.append(n[i+1])
        # print(res)
        return res
            
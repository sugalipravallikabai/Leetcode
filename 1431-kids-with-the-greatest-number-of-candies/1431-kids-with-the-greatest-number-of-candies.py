class Solution:
    def kidsWithCandies(self, can : List[int], ex : int) -> List[bool]:
        
        res = []
        
        for i in range(len(can)):
            
            x = can[i] + ex
            
            if x >= max(can):
                res.append(True)
            else:
                res.append(False)
        return res
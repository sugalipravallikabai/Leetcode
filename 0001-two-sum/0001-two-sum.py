class Solution:
    def twoSum(self, n : List[int], t : int) -> List[int]:
        m = len(n)
        d = {}
        for i in range(m):
            if t - n[i] in d:
                return [d[t-n[i]],i]
            d[n[i]] = i
        return [-1,-1]
        
                
            
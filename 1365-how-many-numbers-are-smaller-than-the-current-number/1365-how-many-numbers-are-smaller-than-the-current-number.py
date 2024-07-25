class Solution:
    def smallerNumbersThanCurrent(self, num: List[int]) -> List[int]:
        
        n = sorted(num)
        d={}
        for i,k in enumerate(n):
            
            if k not in d:
                
                d[k] = i
                
        res = [d[i] for i in num]
        
        return res
        
class Solution:
    def buildArray(self, n : List[int]) -> List[int]:
        
        k = [0] * len(n)
        
        for i in range(len(n)):
            
            k[i] = n[n[i]]
            
        return k
        
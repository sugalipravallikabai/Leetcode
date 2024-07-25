class Solution:
    def sumIndicesWithKSetBits(self, n : List[int], k: int) -> int:
        
        tol = 0
        for i in range(len(n)):
            
            if bin(i).count('1') == k:
                
                tol +=  n[i]
                
        return tol
        
        
        
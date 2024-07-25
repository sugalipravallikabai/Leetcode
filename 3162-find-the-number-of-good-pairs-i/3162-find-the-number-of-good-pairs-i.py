class Solution:
    def numberOfPairs(self, n1: List[int], n2: List[int], k: int) -> int:
        
        cnt = 0
        for i in range(len(n1)):
            
            for j in range(len(n2)):
                
                if n1[i] % (n2[j]*k) == 0:
                    
                    cnt += 1
        return cnt
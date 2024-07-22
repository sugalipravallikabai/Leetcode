class Solution:
    def minimumOperations(self, n : List[int]) -> int:
        
        cnt = 0
        
        for i in range(len(n)):
            
            if (n[i]+1) % 3 == 0:
                
                cnt+=1
            elif (n[i]-1) % 3 == 0:
                cnt += 1
        return cnt
        
        
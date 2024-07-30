class Solution:
    def twoSum(self, n : List[int], t : int) -> List[int]:
        
        
        for i in range(len(n)):
            if i > 0 and n[i] == n[i-1]:
                continue
            
            for j in range(i+1,len(n)):
                
                if j > i+1 and n[j] == n[j-1]:
                    continue
                
                if n[i]+n[j] == t:
                    
                    return [i,j]
                
            
class Solution:
    def numberOfEmployeesWhoMetTarget(self, h : List[int], t : int) -> int:
        
        cnt = 0
        
        for i in range(len(h)):
            
            if h[i] >= t:
                
                cnt+=1
        return cnt
class Solution:
    def maximumWealth(self, a : List[List[int]]) -> int:
        
        maxi = 0
        
        for i in range(len(a)):
            
            maxi = max(maxi , sum(a[i]))
            
        return maxi
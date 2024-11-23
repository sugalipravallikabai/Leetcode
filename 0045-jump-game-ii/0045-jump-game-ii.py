class Solution:
    def jump(self, num : List[int]) -> int:
        
        n = len(num)
        l = r = 0
        jump = 0
        while r < n-1:
            
            farthest = 0 
            for i in range(l,r+1):
                farthest = max(i+num[i],farthest)
            l = r+1
            r = farthest
            jump += 1
        return jump
            
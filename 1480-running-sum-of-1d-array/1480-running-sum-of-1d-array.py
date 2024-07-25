class Solution:
    def runningSum(self, n : List[int]) -> List[int]:
        
        tol = 0
        for i in range(len(n)):
            
            tol += n[i]
            n[i] = tol
        return n
            
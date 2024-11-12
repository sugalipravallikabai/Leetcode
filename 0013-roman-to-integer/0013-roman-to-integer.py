class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I' : '1',
            'V' : '5',
            'X' : '10',
            'L' : '50',
            'C' : '100',
            'D' : '500',
            'M' : '1000'
        }
        
        val = 0
        tol = 0
        for c in reversed(s):
            if val > int(d[c]):
                tol -= int(d[c])
            else :
                tol += int(d[c])
            val = int(d[c])
        
        return tol
            
            
            
            
            
            
            
            
            
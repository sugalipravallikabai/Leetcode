class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        dg = 1
        
        for node in preorder.split(','):
            dg -= 1
            if dg < 0:
                return False
            if node != '#':
                dg += 2
            
        return dg == 0
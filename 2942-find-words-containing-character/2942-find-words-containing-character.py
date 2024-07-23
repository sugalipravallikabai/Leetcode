class Solution:
    def findWordsContaining(self, w: List[str], x: str) -> List[int]:
        
        res = []
        
        for i in range(len(w)):
            
            for j in range(len(w[i])):
                
                if w[i][j] == x:
                    
                    res.append(i)
                    break
        return res
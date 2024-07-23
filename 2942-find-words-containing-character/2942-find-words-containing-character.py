class Solution:
    def findWordsContaining(self, w: List[str], x: str) -> List[int]:
        
        res = []
        
        for i in range(len(w)):
            
            if x in w[i]:
                
                res.append(i)
        return res
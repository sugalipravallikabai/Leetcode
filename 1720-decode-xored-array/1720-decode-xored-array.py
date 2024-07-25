class Solution:
    def decode(self, e : List[int], f: int) -> List[int]:
        
        res = [0]*(len(e)+1)
        res[0] = f
        for i in range(len(e)):
            x = e[i] ^ res[i]
            res[i+1] = x
        return res
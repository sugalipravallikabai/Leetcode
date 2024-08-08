class Solution:
    def findArray(self, p: List[int]) -> List[int]:
        n = len(p)
        res = [0]*n
        x = 0
        for i in range(len(p)):
            res[i] = p[i] ^ x
            x ^= res[i]
        return res

        
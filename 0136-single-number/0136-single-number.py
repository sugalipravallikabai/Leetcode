class Solution:
    def singleNumber(self, n : List[int]) -> int:
        xor = 0
        for i in range(len(n)):
            xor ^= n[i]
        return xor
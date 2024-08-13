class Solution:
    def minOperations(self, n : List[int], k: int) -> int:
        x = 0
        for i in n:
            x ^= i
        return bin(x^k).count('1')
        
class Solution:
    def missingNumber(self, n : List[int]) -> int:
        x = 0
        x1 = 0
        for i in range(len(n)):
            x ^= n[i]
            x1 ^= i+1

        return x ^ x1
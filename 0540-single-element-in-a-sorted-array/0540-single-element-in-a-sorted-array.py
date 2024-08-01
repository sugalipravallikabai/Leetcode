class Solution:
    def singleNonDuplicate(self, n : List[int]) -> int:
        x = 0
        for i in range(len(n)):
            x ^= n[i]
        return x
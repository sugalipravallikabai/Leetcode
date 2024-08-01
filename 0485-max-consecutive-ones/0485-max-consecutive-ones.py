class Solution:
    def findMaxConsecutiveOnes(self, n : List[int]) -> int:
        c = 0
        m = 0
        for i in range(len(n)):
            if n[i] == 1:
                c += 1
                if m < c:
                    m = c
            else:
                c = 0
        return m
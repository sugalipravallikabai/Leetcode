class Solution:
    def findMaxConsecutiveOnes(self, n : List[int]) -> int:
        cnt = 0
        m = 0
        for i in range(len(n)):
            if n[i] == 1:
                cnt += 1
                m = max(m,cnt)
            else:
                cnt = 0
        return m
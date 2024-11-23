class Solution:
    def canJump(self, n : List[int]) -> bool:
        if len(n) == 1:
            return True
        m = 0
        for i in range(len(n)):
            if i > m:
                return False
            m = max(m,i+n[i])
        return True
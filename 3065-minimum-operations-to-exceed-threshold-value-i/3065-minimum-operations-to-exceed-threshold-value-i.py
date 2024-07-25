class Solution:
    def minOperations(self, n : List[int], k: int) -> int:
        n.sort()
        cnt = 0
        for i in range(len(n)):
            
            if min(n) < k:
                cnt += 1
                n.pop(0)
            else:
                return cnt
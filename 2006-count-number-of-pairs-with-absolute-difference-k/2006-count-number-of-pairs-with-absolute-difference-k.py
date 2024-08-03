class Solution:
    def countKDifference(self, n : List[int], k: int) -> int:
        cnt = 0
        for i in range(len(n)):
            for j in range(i):
                if abs(n[i]-n[j]) == k:
                    cnt += 1
        return cnt
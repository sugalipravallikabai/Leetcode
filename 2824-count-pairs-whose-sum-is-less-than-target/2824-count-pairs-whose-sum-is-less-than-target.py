class Solution:
    def countPairs(self, n : List[int], target: int) -> int:
        
        cnt = 0
        n.sort()
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i]+n[j] < target:
                    cnt += 1
                else:
                    break
        return cnt
        
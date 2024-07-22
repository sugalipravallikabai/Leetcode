class Solution:
    def numIdenticalPairs(self, n : List[int]) -> int:
        
        cnt = 0
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i] == n[j]:
                    cnt += 1
        return cnt
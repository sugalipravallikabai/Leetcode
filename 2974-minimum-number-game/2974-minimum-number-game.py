class Solution:
    def numberGame(self, n : List[int]) -> List[int]:
        n.sort()
        for i in range(0,len(n),2):
            n[i],n[i+1] = n[i+1],n[i]
        return n
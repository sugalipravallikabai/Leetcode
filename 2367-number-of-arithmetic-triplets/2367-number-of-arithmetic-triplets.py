class Solution:
    def arithmeticTriplets(self, n : List[int], d : int) -> int:
        cnt = 0
        m = len(n)
        for i in range(m):
            for j in range(i+1,m):
                for k in range(j+1,m):
                    if n[j]-n[i] == n[k]-n[j] == d :
                        cnt+=1
        return cnt
        
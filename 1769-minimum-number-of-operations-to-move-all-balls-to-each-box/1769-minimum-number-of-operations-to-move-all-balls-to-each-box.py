class Solution:
    def minOperations(self, b : str) -> List[int]:
        l = []
        res = []
        for i in b:
            l.append(int(i))
        
        for i in range(len(l)):
            tol = 0
            for j in range(len(l)):
                if j != i and l[j] == 1:
                    tol += abs(j-i)
            res.append(tol)
        return res
            
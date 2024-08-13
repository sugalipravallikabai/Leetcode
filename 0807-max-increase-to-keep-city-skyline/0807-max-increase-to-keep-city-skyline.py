class Solution:
    def maxIncreaseKeepingSkyline(self, g : List[List[int]]) -> int:
        n = len(g)
        r = [max(x) for x in g]
        c = [max(y) for y in zip(*g)]
        tol = 0
        for i in range(n):
            for j in range(n):
                tol += min(r[i],c[j])-g[i][j]
        return tol
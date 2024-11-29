class Solution:
    def findMaxFish(self, g : List[List[int]]) -> int:
        n,m = len(g),len(g[0])
        visit = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0
        def fun(i,j):
            visit[i][j] = 1
            res = g[i][j]
            dr = [0,1,0,-1]
            dc = [-1,0,1,0]
            for k in range(4):
                r = dr[k]+i
                c = dc[k]+j
                if (r >= 0 and r < n) and (c >= 0 and c < m) and (visit[r][c] != 1 and g[r][c] != 0) :
                    res += fun(r,c)
            return res
        for i in range(n):
            for j in range(m):
                if g[i][j] != 0 and visit[i][j] != 1:
                    ans = max(ans,fun(i,j))
        return ans
                    
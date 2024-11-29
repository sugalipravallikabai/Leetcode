class Solution:
    def numIslands(self, g : List[List[str]]) -> int:
        n,m = len(g),len(g[0])
        visit = [[0 for _ in range(m)] for j in range(n)]
        cnt = 0
        def fun(i,j):
            visit[i][j] = 1
            dr = [0,1,0,-1]
            dc = [1,0,-1,0]
            for k in range(4):
                r = i+dr[k]
                c = j+dc[k]
                if (r >= 0 and r < n) and (c >= 0 and c < m) and (visit[r][c] != 1 and g[r][c] == '1'):
                    fun(r,c)
        for i in range(n):
            for j in range(m):
                if visit[i][j] != 1 and g[i][j] == '1':
                    fun(i,j)
                    cnt += 1
        return cnt
            
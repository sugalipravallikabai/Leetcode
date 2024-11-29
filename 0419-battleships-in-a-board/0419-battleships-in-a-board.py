class Solution:
    def countBattleships(self, b : List[List[str]]) -> int:
        n,m = len(b),len(b[0])
        visit = [[0 for _ in range(m)] for _ in range(n)]
        cnt = 0
        def fun(i,j):
            visit[i][j] = 1
            dr = [0,-1,0,1]
            dc = [1,0,-1,0]
            for k in range(4):
                r = dr[k]+i
                c = dc[k]+j
                if (r >= 0 and r < n) and (c >= 0 and c < m) and visit[r][c] != 1 and b[r][c] == 'X':
                    fun(r,c)
        for i in range(n):
            for j in range(m):
                if b[i][j] == 'X' and visit[i][j] != 1:
                    fun(i,j)
                    cnt += 1
        return cnt
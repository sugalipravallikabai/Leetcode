class Solution:
    def solve(self, b : List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not b or not b[0]:
            return b
        n,m = len(b) , len(b[0])
        visit = [[0]*m for _ in range(n)]
        
        def dfs(r,c,v,b):
            
            v[r][c] = 1
            
            for dr,dc in ([-1,0],[1,0],[0,-1],[0,1]):
                row = r+dr
                col = c+dc
                
                if 0 <= row < n and  0 <= col < m and v[row][col] != 1 and b[row][col] == 'O':
                    dfs(row,col,v,b)
        
        for j in range(m):
            
            if visit[0][j] != 1 and b[0][j] == 'O':
                
                dfs(0,j,visit,b)
            
            if visit[n-1][j] != 1 and b[n-1][j] == 'O':
                
                dfs(n-1,j,visit,b)
        
        for i in range(n):
            
            if visit[i][0] != 1 and b[i][0] == 'O':
                
                dfs(i,0,visit,b)
                
            if visit[i][m-1] != 1 and b[i][m-1] == 'O':
                
                dfs(i,m-1,visit,b)
        
        for i in range(n):
            for j in range(m):
                if b[i][j] == 'O' and visit[i][j] == 0:
                    
                    b[i][j] = 'X'
        
        return b
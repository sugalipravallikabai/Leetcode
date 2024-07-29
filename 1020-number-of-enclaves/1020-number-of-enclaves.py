class Solution:
    def numEnclaves(self, g : List[List[int]]) -> int:
        if not g or not g[0]:
            return 0
        
        n,m = len(g),len(g[0])
        v = [[0]*m for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and g[i][j] == 1:
                    
                    v[i][j] = 1
                    q.append([i,j])
        
        while len(q) != 0:
            
            r,c = q.popleft()
            
            for dr,dc in ([-1,0],[1,0],[0,-1],[0,1]):
                
                row = r+dr
                col = c+dc
                
                if 0 <= row < n and 0 <= col < m and v[row][col] != 1 and g[row][col] ==1:
                    q.append([row,col])
                    v[row][col] = 1
        cnt = 0
        
        for i in range(n):
            for j in range(m):
                if g[i][j] == 1 and v[i][j] == 0:
                    
                    cnt += 1
        
        return cnt
        
        
        
        

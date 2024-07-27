class Solution:
    def orangesRotting(self, g : List[List[int]]) -> int:
        n,m = len(g),len(g[0])

        time , fresh = 0 , 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    fresh += 1
                elif g[i][j] == 2:
                    q.append([i,j])
        
        while q and fresh > 0:
            
            for i in range(len(q)):

                r,c = q.popleft()

                for dr,dc in ([1,0],[-1,0],[0,1],[0,-1]):

                    row = dr+r
                    col = dc+c

                    if row < 0 or col < 0 or row == n or col == m or g[row][col] != 1:
                        continue
                    
                    g[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

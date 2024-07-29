class Solution:
    def updateMatrix(self, mat : List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        n,m = len(mat),len(mat[0])
        q = deque()
        maxi = n*m
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = maxi
        
        while q:
            r,c = q.popleft()
            for dr,dc in ([-1,0],[1,0],[0,-1],[0,1]):
                row = r+ dr
                col = c + dc
                if 0 <= row < n and 0 <= col < m and mat[row][col] > mat[r][c]+1:
                    q.append([row,col])
                    mat[row][col] = mat[r][c]+1
        return mat
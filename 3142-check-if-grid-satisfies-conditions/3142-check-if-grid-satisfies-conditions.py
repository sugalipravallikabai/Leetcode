class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        def fun(i,j):
            k = i+1
            l = j+1
            if k < n :
                if grid[i][j] != grid[k][j]:
                    return False
            if  l < m  and  grid[i][j] == grid[i][l]:
                return False
            return True
            
        for i in range(n):
            for j in range(m):
                if not fun(i,j):
                    return False
        return True
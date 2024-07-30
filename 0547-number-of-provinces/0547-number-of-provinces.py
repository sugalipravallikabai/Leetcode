class Solution:
    def findCircleNum(self, a : List[List[int]]) -> int:
        
        if not a:
            return 0
        
        n = len(a)
        temp = [0]*n
        cnt = 0
        
        def dfs(x):
            # temp[x] = 1
            for j in range(n):
                if a[x][j] == 1 and temp[j] != 1:
                    temp[j] = 1
                    dfs(j)
        
        for i in range(n):
            if temp[i] == 0:
                dfs(i)
                temp[i] = 1
                cnt+=1
        return cnt
            
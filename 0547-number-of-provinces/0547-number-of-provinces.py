class Solution:
    def findCircleNum(self, a : List[List[int]]) -> int:

        if  not a:
            return 0
        n = len(a)
        temp = [0] * n
        
        def dfs(i):
            for j in range(n):
                if a[i][j] == 1 and temp[j] != 1:
                    temp[j] = 1
                    dfs(j)
        
        cnt = 0
        for i in range(n):
            if temp[i] == 0:
                temp[i] = 1
                cnt += 1
                dfs(i)
                
        return cnt
                
class Solution:
    def findCircleNum(self, icon : List[List[int]]) -> int:
        n = len(icon)
        visit = [0]*n
        cnt  = 0
        def fun(r):
            visit[r] = 1
            for j in range(n):
                if visit[j] != 1 and icon[r][j] == 1:
                    fun(j)
        for i in range(n):
            if visit[i] != 1 :
                    cnt += 1
                    fun(i)
        return cnt
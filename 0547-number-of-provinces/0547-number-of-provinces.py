class Solution:
    def findCircleNum(self, a : List[List[int]]) -> int:
        
        if not a:
            return 0
        
        n = len(a)
        temp = [0]*n
        cnt = 0
        q = deque()
        
        def bfs(x):
            q.append(x)
            while q:
                node = q.popleft()
                temp[node] = 1
                for j in range(n):
                    if a[node][j] == 1 and temp[j] !=1:
                        q.append(j)
                        temp[j] = 1
            
        
        for i in range(n):
            if temp[i] == 0:
                bfs(i)
                # tem[i] = 1
                cnt += 1
        return cnt
            
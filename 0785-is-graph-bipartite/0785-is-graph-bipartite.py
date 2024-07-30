class Solution:
    def isBipartite(self, g : List[List[int]]) -> bool:
        n = len(g)
        c = [0]*n
        q = deque()
        for i in range(n):
            if c[i] != 0:
                continue
            q.append(i)
            c[i] = 1
            
            while q :
                cur = q.popleft()
                for val in g[cur]:
                    if c[val] == 0 :
                        c[val] = -c[cur]
                        q.append(val)
                    elif c[val] == c[cur]:
                        return False
        return True
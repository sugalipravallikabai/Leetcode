class Solution:
    def isBipartite(self, g : List[List[int]]) -> bool:
        n = len(g)
        c = [0]*n
        
        def dfs(node,col,c,g):
            c[node] = col
            
            for val in g[node]:
                if c[val] == 0:
                    if not dfs(val , -col , c, g):
                        return False
                elif c[val] == c[node]:
                    return False
            return True
        
        for i in range(n):
            if c[i] == 0:
                if dfs(i,1,c,g) == False:
                    return False
        return True
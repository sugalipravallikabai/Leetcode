from collections import deque,defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ing: List[List[str]], sup: List[str]) -> List[str]:
        res = []
        s = set(sup)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for rec,ingredients in zip(recipes,ing):
            for ingred in ingredients:
                if ingred not in s:
                    graph[ingred].append(rec)
                    indegree[rec]+=1
        que = deque(recip for recip in recipes if indegree[recip] == 0)
        
        while que:
            current = que.popleft()
            res.append(current)
            for ingred in graph[current]:
                indegree[ingred] -= 1
                if indegree[ingred] == 0:
                    que.append(ingred)
        return res
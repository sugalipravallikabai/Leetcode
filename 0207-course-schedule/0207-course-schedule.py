from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] += 1
            
        que = deque(i for i in range(numCourses) if indegree[i] == 0)
        cnt = 0
        while que:
            node = que.popleft()
            cnt += 1
            for j in adj[node]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    que.append(j)
        if cnt == numCourses:
            return True
        return False
            
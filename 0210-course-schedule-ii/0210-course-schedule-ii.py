class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]]+=1
        
        que = deque(i for i in range(numCourses) if indegree[i] == 0)
        print(que)
        cnt = 0
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)
            for j in adj[node]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    que.append(j)
        return ans if len(ans) == numCourses else []
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        que = []
        tol = 0
        for dur,last in courses:
            tol += dur
            heapq.heappush(que,-dur)
            if tol > last:
                tol += heapq.heappop(que)
        return len(que)
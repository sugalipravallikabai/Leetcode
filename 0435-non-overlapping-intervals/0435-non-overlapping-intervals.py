class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 1
        n = len(intervals)
        intervals.sort(key = lambda x:x[1])
        print(intervals)
        st = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,n):
            if end <= intervals[i][0]:
                cnt += 1
                st = intervals[i][0]
                end = intervals[i][1]
                
        return n - cnt
            
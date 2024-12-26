class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
#        [[1,3],[2,4]]
#       [[1,3],[5,7],[9,10]]
#       [[3,5],[6,10],[8,11],[14,20]]  days = 22

#        [[3,49],[3,31],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48]] days = 57
        cnt = 0
        meetings.sort(key = lambda x: x[0])
        n = len(meetings)
        ans = []
        st = meetings[0][0]
        end = meetings[0][1]
        ans.append(meetings[0])
        for i in range(1,n):
            if end >= meetings[i][0]:
                st = min(st,meetings[i][0]) 
                end = max(end,meetings[i][1])
                ans[-1][1] = end
            else:
                ans.append([meetings[i][0],meetings[i][1]])
                st = meetings[i][0]
                end = meetings[i][1] 
        n = len(ans)
        print(ans)
        if ans[0][0] != 1:
            cnt += (ans[0][0]-1)
        if ans[n-1][1] != days:
            cnt += (days - ans[n-1][1])
        for i in range(1,n):
            if ans[i-1][1] < ans[i][0]:
                cnt += (ans[i][0]-ans[i-1][1]-1)
            
        return cnt
    
    
    
    
    
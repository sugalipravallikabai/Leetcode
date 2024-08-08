class Solution:
    def countPoints(self, p : List[List[int]], q : List[List[int]]) -> List[int]:
        
        res = []
        
        for i in range(len(q)):
            cnt = 0
            for j in range(len(p)):
                t = sqrt(((q[i][0]-p[j][0])**2 )+ ((q[i][1]-p[j][1]))**2)
                if t <= q[i][2]:
                    cnt += 1
            res.append(cnt)
        return res
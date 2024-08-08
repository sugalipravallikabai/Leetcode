from collections import defaultdict
class Solution:
    def findMatrix(self, n : List[int]) -> List[List[int]]:
        m = len(n)
        d = defaultdict(list)
        for i in range(m):
            k = 0
            while k < m:
                if n[i] not in d[k]:
                    d[k].append(n[i])
                    break
                k+=1
        res = []
        for k,v in d.items():
            res.append(v)
        return res
        
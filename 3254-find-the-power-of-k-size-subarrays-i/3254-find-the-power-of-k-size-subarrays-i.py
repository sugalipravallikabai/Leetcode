class Solution:
    def resultsArray(self, n : List[int], k: int) -> List[int]:
        t = []
        for i in range(len(n)-k+1):
            t.append(n[i:i+k])
        res = [-1]*len(t)
        for i in range(len(t)):
            v = t[i]
            flag = True
            for j in range(1,len(v)):
                if v[j-1]+1 != v[j]:
                    flag = False
                    break
            if flag:
                res[i] = t[i][-1]
        return res
                
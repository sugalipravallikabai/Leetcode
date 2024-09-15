class Solution:
    def merge(self, a : List[List[int]]) -> List[List[int]]:
        t = []
        a.sort()
        for i in range(len(a)):
            if not t or a[i][0] > t[-1][1]:
                t.append(a[i])
            else:
                t[-1][1] = max(t[-1][1],a[i][1])
        return t
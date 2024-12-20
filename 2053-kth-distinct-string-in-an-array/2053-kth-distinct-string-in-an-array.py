# form collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l = []
        d = Counter(arr)
        for i in d:
            if d[i] == 1:
                l.append(i)
        if len(l) < k:
            return ''
        return l[k-1]
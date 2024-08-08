from collections import defaultdict

class Solution:
    def groupThePeople(self, g : List[int]) -> List[List[int]]:
        
        d = defaultdict(list)
        for ind , size in enumerate(g):
            d[size].append(ind)
        
        grp = []
        for gs , li in d.items():
            while len(li) >= gs:
                sub = li [ : gs]
                grp.append(sub)
                li = li[gs:]
        return grp
        
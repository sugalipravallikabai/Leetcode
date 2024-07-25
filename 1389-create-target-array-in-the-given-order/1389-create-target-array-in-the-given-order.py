class Solution:
    def createTargetArray(self, n : List[int], ind : List[int]) -> List[int]:
        res = []
        for i,j in zip(n,ind):
            res.insert(j,i)
        return res
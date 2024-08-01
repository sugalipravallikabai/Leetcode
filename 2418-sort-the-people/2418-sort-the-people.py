class Solution:
    def sortPeople(self, n : List[str], h : List[int]) -> List[str]:
        
        res = []
        
        for i,j in zip(n,h):
            res.append([j,i])
        res.sort(reverse = True)
        ans = []
        for k in range(len(res)):
            ans.append(res[k][1])
        return ans
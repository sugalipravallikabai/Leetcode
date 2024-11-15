class Solution:
    def merge(self, inter : List[List[int]]) -> List[List[int]]:
        
        ans  = []
        inter.sort()
        for i in range(len(inter)):
            if not ans or ans[-1][1] < inter[i][0]:
                ans.append(inter[i])
            elif ans[-1][1] >= inter[i][0]:
                ans[-1][1] = max(ans[-1][1],inter[i][1])
        return ans
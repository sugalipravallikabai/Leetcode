class Solution:
    def combinationSum(self, c : List[int], t : int) -> List[List[int]]:
        def find(c,ind,ans,temp,s,t):
            if s == t :
                ans.append(temp.copy())
                return
            if s > t or ind == len(c):
                return
            temp.append(c[ind])
            find(c,ind,ans,temp,s+c[ind],t)
            temp.pop()
            find(c,ind+1,ans,temp,s,t)

        ans = []
        temp = []
        find(c,0,ans,temp,0,t)
        return ans
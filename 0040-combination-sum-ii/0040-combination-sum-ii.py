class Solution:
    def combinationSum2(self, c : List[int], t : int) -> List[List[int]]:
        
        def fun(n,ind,temp,ans,t):
            
            if  t < 0:
                return 
            if t == 0:
                ans.append(temp.copy())
                return
            for i in range(ind,len(n)):
                if i > ind and n[i] == n[i-1]:
                    continue
                temp.append(n[i])
                fun(n,i+1,temp,ans,t-n[i])
                temp.pop()
        c.sort()
        ans = []
        fun(c,0,[],ans,t)
        return ans

        
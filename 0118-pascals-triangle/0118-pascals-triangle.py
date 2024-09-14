class Solution:
    def generate(self, n: int) -> List[List[int]]:
        def fun(row):
            ans=[1]
            val = 1
            for i in range(1,row):
                val *= (row-i)
                val //= (i)
                ans.append(val)
            return ans
        
        a = []
        for i in range(1,n+1):
            a.append(fun(i))
        return a
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fun(r):
            temp = []
            temp.append(1)
            res = 1
            for i in range(0,r):
                res = res * (r-i)
                res = res//(i+1)
                temp.append(res)
            return temp
        
        ans = []
        for i in range(numRows):
            ans.append(fun(i))
        return ans
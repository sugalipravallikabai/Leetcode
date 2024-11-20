class Solution:
    def getRow(self, r: int) -> List[int]:
        ans = []
        ans.append(1)
        for i in range(r):
            res = ans[-1]*(r-i)
            res = res//(i+1)
            ans.append(res)
        return ans
        
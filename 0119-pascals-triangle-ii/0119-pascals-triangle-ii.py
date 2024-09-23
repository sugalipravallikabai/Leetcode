class Solution:
    def getRow(self, r : int) -> List[int]:
        
        if r == 0:
            return [1]
        ans = []
        ans.append(1)
        val = 1
        r=r+1
        for i in range(1,r):
            val *= (r-i)
            val //= i
            ans.append(val)
        return ans
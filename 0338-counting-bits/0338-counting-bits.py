class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            val = bin(i)
            ans.append(val.count('1'))
        return ans
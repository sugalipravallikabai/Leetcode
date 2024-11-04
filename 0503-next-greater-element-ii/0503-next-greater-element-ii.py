class Solution:
    def nextGreaterElements(self, n: List[int]) -> List[int]:
        m = len(n)
        ans = [-1] * m
        for i in range(m):
            for j in range(i+1,i+m):
                ind = j % m
                if n[i] < n[ind]:
                    ans[i] = n[ind]
                    break
        return ans
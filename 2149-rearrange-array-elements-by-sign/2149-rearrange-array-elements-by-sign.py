class Solution:
    def rearrangeArray(self, n : List[int]) -> List[int]:
        
        ans = [0]*len(n)
        pos = 0
        neg = 1
        for i in range(len(n)):
            if n[i] > 0:
                ans[pos] = n[i]
                pos += 2
            else:
                ans[neg] = n[i]
                neg += 2
        return ans
            
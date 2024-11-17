class Solution:
    def findLengthOfShortestSubarray(self, a : List[int]) -> int:
        r = len(a)-1
        n = len(a)
        while r > 0 and a[r] >= a[r-1]:
            r -= 1
        l = 0
        ans = r
        while l < r and (l == 0 or (a[l-1] <= a[l])):
            
            while r < n and a[l] > a[r] :
                r += 1
            ans = min(ans,r-l-1)
            l += 1
            
        return ans
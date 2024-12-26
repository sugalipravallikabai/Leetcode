class Solution:
    def maxArea(self, h : List[int]) -> int:
        l,r = 0, len(h)-1
        maxi = 0
        while l < r:
            height = min(h[l],h[r])
            width = r-l
            cur = height*width
            maxi = max(maxi,cur)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return maxi
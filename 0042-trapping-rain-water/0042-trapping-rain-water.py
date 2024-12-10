class Solution:
    def trap(self, height: List[int]) -> int:
        # no negative integers
        # linear data structure
        l,r = 0,len(height)-1
        tol = 0
        lmax,rmax=0,0
        while l < r:
            if height[l] <= height[r]:
                if lmax > height[l]:
                    tol += lmax-height[l]
                else:
                    lmax = max(lmax,height[l])
                l = l+1
            else:
                if rmax > height[r]:
                    tol += rmax-height[r]
                else:
                    rmax = max(rmax,height[r])
                r = r-1
        return tol
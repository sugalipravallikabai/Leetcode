class Solution:
    def trap(self, h : List[int]) -> int:
        
        n = len(h)
        lmax , rmax = 0,0
        tol , l , r = 0,0,n-1
        while l < r:
            if h[l] <= h[r]:
                if lmax >= h[l]:
                    tol += lmax-h[l]
                else:
                    lmax = h[l]
                l += 1
            else:
                if rmax >= h[r]:
                    tol += rmax-h[r]
                else:
                    rmax = h[r]
                r -= 1
        return tol
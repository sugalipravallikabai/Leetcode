class Solution:
    def maxArea(self, h : List[int]) -> int:
        
        left,right = 0,len(h)-1
        maxi = 0
        while left < right:
            width = right-left
            mini = min(h[left],h[right])
            curr = width*mini
            
            maxi = max(curr,maxi)
            
            if h[left]<h[right]:
                left += 1
            else:
                right -= 1
        return maxi
class Solution:
    def spiralOrder(self, a : List[List[int]]) -> List[int]:
        ans  = []
        left = top = 0
        n = len(a)
        m = len(a[0])
        right = m-1
        bottom = n-1
        while top <= bottom and left <= right:
            
            for i in range(left,right+1):
                ans.append(a[top][i])
            top += 1
            for i in range(top,bottom+1):
                ans.append(a[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(a[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans.append(a[i][left])
                left += 1
        return ans
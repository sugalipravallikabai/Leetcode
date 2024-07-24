class Solution:
    def spiralOrder(self, m : List[List[int]]) -> List[int]:
        
        r,c = len(m),len(m[0])
        left = 0
        right = c-1
        top = 0
        btm = r-1
        ans = []
        
        while top <= btm and left <= right:
            for i in range(left,right+1):
                ans.append(m[top][i])
            top += 1
            if not (top <= btm and left <= right):
                break
            for i in range(top,btm+1):
                ans.append(m[i][right])
            right -= 1
            if not (top <= btm and left <= right):
                break
            for i in range(right,left-1,-1):
                ans.append(m[btm][i])
            btm -= 1
            if not (top <= btm and left <= right):
                break
            for i in range(btm,top-1,-1):
                ans.append(m[i][left])
            left += 1
            
        return ans
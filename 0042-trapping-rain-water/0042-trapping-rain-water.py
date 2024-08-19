class Solution:
    def trap(self, h : List[int]) -> int:
        
        n= len(h)
        pre = []
        suf = [0]*n
        pre.append(h[0])
        suf[n-1] = h[n-1]
        tol = 0
        for i in range(1,n):
            x = max(pre[-1],h[i])
            pre.append(x)
        for i in range(n-2,-1,-1):
            x = max(suf[i+1],h[i])
            suf[i]=x
        for i in range(n):
            if h[i] < pre[i] and h[i] < suf[i]:
                tol += min(pre[i],suf[i])-h[i]
        return tol
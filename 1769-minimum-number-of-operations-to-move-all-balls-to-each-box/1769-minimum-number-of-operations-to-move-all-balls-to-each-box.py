class Solution:
    def minOperations(self, b : str) -> List[int]:
        
        n = len(b)
        pl = [0]*n
        pr = [0]*n
        cnt = 0
        for i in range(n):
            if i > 0:
                pl[i] = pl[i-1] + cnt
            if b[i] == '1':
                cnt += 1
        cnt = 0
        for i in range(n-1,-1,-1):
            if i < n-1:
                pr[i] = pr[i+1]+cnt
            if b[i] == '1':
                cnt += 1 
        res = [pl[i]+pr[i] for i in range(n)]
        return res
        
            
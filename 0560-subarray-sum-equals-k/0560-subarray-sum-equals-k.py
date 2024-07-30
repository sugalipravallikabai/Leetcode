class Solution:
    def subarraySum(self, a : List[int], k: int) -> int:
        
        #  applicable only for positive numbers....
        
#         cnt = 0
#         tol = a[0]
#         n = len(a)
#         i,j = 0,0
        
#         if n == 1:
#             if tol != k:
#                 return 0
        
#         while j < n:
#             while tol > k and i <= j:
                
#                 tol -= a[i]
#                 i+=1
#             if tol == k:
#                 cnt += 1
#             j+=1
#             if j < n:
#                 tol += a[j]
        # return cnt
        
        cnt = 0
        d = {}
        ps = 0
        n = len(a)
        
        for i in range(n):
            ps += a[i]
            
            if ps == k:
                cnt += 1
            if ps-k in d:
                cnt +=  d[ps-k]
            if ps not in d:
                d[ps] = 1
            else:
                d[ps] += 1
        return cnt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
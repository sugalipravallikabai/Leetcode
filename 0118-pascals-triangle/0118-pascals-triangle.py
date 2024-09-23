class Solution:
    def generate(self, n: int) -> List[List[int]]:
#         def fun(row):
#             ans = []
#             ans.append(1)
#             val = 1
#             for i in range(1,row):
#                 val *= (row-i)
#                 val //= i
#                 ans.append(val)
#             return ans
        
#         a = []
#         for i in range(1,n+1):
        #     a.append(fun(i))
        # return a
        


#           using dp approch
        t = []
        
        for i in range(n):
            row = [1]*(i+1)
            
            for j in range(1,i):
                row[j] = t[i-1][j-1]+t[i-1][j]
            
            t.append(row)
        
        return t
    
    
    
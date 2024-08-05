
class Solution:
    def diagonalPrime(self, n : List[List[int]]) -> int:
        
        maxi = 0
        d = []
        for i in range(len(n)):
            if i < len(n):
                d.append(n[i][i])
                maxi = max(maxi,n[i][i])
            if i < len(n):
                d.append(n[i][len(n)-1-i])
                maxi = max(maxi,n[i][len(n)-1-i])
        
        temp = [True] * (maxi+1)
        temp[0]=temp[1]= False
        for i in range(isqrt(maxi)+1):
            if temp[i]:
                for j in range(i*i,maxi+1,i):
                    temp[j] = False
        ans = 0
        for val in d:
            if temp[val]:
                ans = max(ans,val)
        return ans
                
        
            
        
class Solution:
    def threeSum(self, n : List[int]) -> List[List[int]]:
        
        res = []
        n.sort()
        
        for i in range(len(n)):
            if i > 0 and n[i]==n[i-1]:
                continue
            if n[i] > 0:
                break
            j = i+1
            k = len(n)-1
            
            while j < k:
                
                tol = n[i]+n[j]+n[k]
                if tol == 0:
                    res.append([n[i],n[j],n[k]])
                    while j < k and n[j] == n[j+1]: j+=1
                    while j < k and n[k] == n[k-1]: k-=1
                    j += 1
                    k -= 1
                elif tol < 0:
                    j += 1
                else:
                    k -= 1
        return res

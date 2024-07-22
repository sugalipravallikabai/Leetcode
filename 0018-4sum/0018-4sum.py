class Solution:
    def fourSum(self, n: List[int], tar: int) -> List[List[int]]:
        n.sort()
        k = []
        
        
        for i in range(len(n)):
            if i > 0 and n[i] == n[i-1] :
                continue
            for j in range(i+1,len(n)):
                if n[j]  == n[j-1] and j > i+1:
                    continue
                l=j+1
                r=len(n)-1
                
                while l < r:
                    tol = n[i] + n[j] + n[l] + n[r]
                    if tol == tar :
                        
                        k.append([n[i],n[j],n[l],n[r]])
                        
                        while l < r and n[l] == n[l+1] :  
                            l+=1
                        while l < r and n[r] == n[r-1] :
                            r-=1
                        l+=1
                        r-=1
                    elif tol < tar:
                        l += 1
                    else:
                        r-=1
        return k
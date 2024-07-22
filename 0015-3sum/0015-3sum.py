class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        k = []
        
        for i in range(len(n)):
            if n[i] == n[i-1] and i > 0:
                continue
            if n[i] > 0:
                break
            l = i+1
            r = len(n)-1
            while l < r:
                if n[i]+n[l]+n[r] == 0:
                    
                    k.append([n[i],n[l],n[r]])
                    
                    while l < r and n[l] == n[l+1]: l+=1
                    while l < r and n[r] == n[r-1]: r-=1
                    l+=1
                    r-=1
                elif n[i]+n[l]+n[r] < 0:
                    l+=1
                else:
                    r-=1
                
        return k


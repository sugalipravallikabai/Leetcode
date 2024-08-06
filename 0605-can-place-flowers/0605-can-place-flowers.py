class Solution:
    def canPlaceFlowers(self, f : List[int], k: int) -> bool:
        
        n = len(f)
        if k == 0:
            return True
        for i in range(n):
            if f[i] == 0:
                if ((i == 0 or f[i-1] == 0) and (i == n-1 or f[i+1] == 0 )):
                    f[i] = 1
                    k -= 1 
                    if k == 0:
                        return True
                
        return k == 0
class Solution:
    def thirdMax(self, n : List[int]) -> int:
        
        if len(n) < 3:
            return max(n)
        n.sort(reverse = True)
        
        cnt = 1
        preele = n[0]
        
        for i in range(len(n)):
            if n[i] != preele:
                cnt += 1
                preele = n[i]
            if cnt == 3:
                return preele
        return n[0]
        
            
        
class Solution:
    def canBeIncreasing(self, n : List[int]) -> bool:
        
        m = len(n)
        removed = False
        for i in range(1,m):
            if n[i-1] >= n[i]:
                if removed:
                    return False
                removed = True
                if i > 1 and n[i-2] >= n[i]:
                    n[i] = n[i-1]
        
        return True
            
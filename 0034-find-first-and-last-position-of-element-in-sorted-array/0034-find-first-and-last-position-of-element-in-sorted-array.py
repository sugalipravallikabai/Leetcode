from typing import List

class Solution:
    def searchRange(self, n: List[int], t: int) -> List[int]:
        s, e = -1, -1
        if not n:
            return [s, e]
        
        l, r = 0, len(n) - 1
        while l <= r:
            m = (l + r) // 2
            if n[m] < t:
                l = m + 1
            elif n[m] > t:
                r = m - 1
            else:
                s = m
                r = m - 1
        
    
        l, r = 0, len(n) - 1
        while l <= r:
            m = (l + r) // 2
            if n[m] < t:
                l = m + 1
            elif n[m] > t:
                r = m - 1
            else:
                e = m
                l = m + 1 
        
        return [s, e]

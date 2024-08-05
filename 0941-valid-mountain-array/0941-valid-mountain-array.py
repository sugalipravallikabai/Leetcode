class Solution:
    def validMountainArray(self, a : List[int]) -> bool:
        
        n = len(a)
        i = 0
        if n < 3:
            return False
        
        while i < n-1 and a[i] < a[i+1]:
            i += 1
        if i == 0 or i == n-1:
            return False
        while i < n-1 and a[i] > a[i+1]:
            i += 1
        return i == n-1
        
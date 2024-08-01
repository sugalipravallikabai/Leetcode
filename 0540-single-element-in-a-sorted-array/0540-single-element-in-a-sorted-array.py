class Solution:
    def singleNonDuplicate(self, n : List[int]) -> int:
        x = 0
        l = 1
        r = len(n)-2
        
        if len(n) == 1:
            return n[0]
        if n[0] != n[1]:
            return n[0]
        if n[len(n)-1] != n[len(n)-2]:
            return n[len(n)-1]
        
        while l <= r:
            m = (l+r)//2
            if n[m] != n[m+1] and n[m] != n[m-1]:
                return n[m]
            elif (m % 2 == 0 and n[m+1] == n[m]) or (m%2 == 1 and n[m-1] == n[m]):
                l = m+1
            else:
                r = m-1
        return -1
class Solution:
    def search(self, n  : List[int], t : int) -> int:
        
        l,r = 0,len(n)-1
        while l <= r:
            m = (l+r)//2
            if n[m] == t:
                return m
            if n[l] <= n[m]:
                if n[l] <= t < n[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if n[m]< t <= n[r]:
                    l = m+1
                else:
                    r = m-1
        return -1

        
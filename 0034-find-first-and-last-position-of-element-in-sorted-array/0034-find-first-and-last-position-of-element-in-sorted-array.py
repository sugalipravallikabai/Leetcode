class Solution(object):
    def searchRange(self, n , t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = -1
        e = -1
        
        l,r = 0,len(n)-1
        while l <= r:
            m = (l+r)//2
            if n[m] == t:
                f = m
                r = m-1
            elif n[m] < t:
                l = m+1
            else:
                r = m-1
        
        l,r = 0,len(n)-1
        while l <= r:
            m = (l+r)//2
            if n[m] == t:
                e = m
                l = m+1
            elif n[m]<t:
                l = m+1
            else:
                r = m-1
                
        return [f,e]
        
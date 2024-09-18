class Solution(object):
    def removeDuplicates(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(n)
        j = 1
        for i in range(1,m):
            if n[i] != n[i-1]:
                n[j] = n[i]
                j+=1
        return j
        
        
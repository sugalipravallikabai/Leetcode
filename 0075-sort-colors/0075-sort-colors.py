class Solution:
    def sortColors(self, n : List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = len(n)-1
        l,m = 0,0
        while m <= h:
            if n[m] == 0:
                n[m],n[l]=n[l],n[m]
                l += 1
                m += 1
            elif n[m] == 1:
                m += 1
            elif n[m] == 2:
                n[h],n[m] = n[m],n[h]
                h -= 1
        return n
        
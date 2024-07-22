class Solution:
    def merge(self, a : List[int], m: int, b : List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        i,j=m-1,n-1
        while i >= 0  and j >= 0:
            if a[i] < b[j]:
                a[last] = b[j]
                j-=1
            else:
                a[last] = a[i]
                i-=1
            last -= 1
        while j >= 0:
            a[last] = b[j]
            j -= 1
            last -= 1
        return a
        
        
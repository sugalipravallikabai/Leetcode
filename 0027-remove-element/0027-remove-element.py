class Solution:
    def removeElement(self, a : List[int], val: int) -> int:
        n = len(a)
        j=0
        for i in range(n):
            if a[i] != val:
                a[j] = a[i]
                j+=1
        return j
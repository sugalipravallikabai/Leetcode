class Solution:
    def nextPermutation(self, a : List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        for i in range(len(a)-2,-1,-1):
            if a[i] < a[i+1]:
                ind = i
                break
        if ind == -1:
            return a.sort()
        for i in range(len(a)-1,ind-1,-1):
            if a[i] > a[ind]:
                a[i],a[ind]=a[ind],a[i]
                break
        a[ind+1:] = sorted(a[ind+1:])
        return a
        
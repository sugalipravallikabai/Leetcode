
class Solution:
    def nextPermutation(self, n : List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        for i in range(len(n)-2,-1,-1):
            if n[i] < n[i+1]:
                ind = i
                break
        if ind == -1:
            n.reverse()
            return n
        for i in range(len(n)-1,ind,-1):
            if n[ind] < n[i]:
                n[i],n[ind]=n[ind],n[i]
                break
        n[ind+1:] = reversed(n[ind+1:])
        return n
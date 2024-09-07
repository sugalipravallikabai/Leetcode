class Solution:
    def moveZeroes(self, n : List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        cnt = 0
        while j < len(n):
            if n[j] != 0:
                n[i] = n[j]
                i += 1
            else:
                cnt += 1
            j += 1
        while i < len(n):
            n[i] = 0
            i += 1
        return n
        
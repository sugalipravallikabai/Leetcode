class Solution:
    def rotate(self, n : List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(n)
        n.reverse()
        n[:k] = reversed(n[:k])
        n[k:] = reversed(n[k:])
        return n
        
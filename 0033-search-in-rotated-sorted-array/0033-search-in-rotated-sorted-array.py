class Solution:
    def search(self, n  : List[int], t : int) -> int:
        for i in range(len(n)):
            if n[i] == t:
                return i
        return -1

        
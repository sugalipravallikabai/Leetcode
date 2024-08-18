class Solution:
    def sortTheStudents(self, s : List[List[int]], k: int) -> List[List[int]]:
        return sorted(s, key = lambda r:r[k],reverse = True)
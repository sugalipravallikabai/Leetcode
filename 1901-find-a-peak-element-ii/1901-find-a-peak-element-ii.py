class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        x, y = 0, len(mat[0]) - 1
        while x < len(mat) or y >= 0:
            if x + 1 < len(mat) and mat[x + 1][y] > mat[x][y]:
                x += 1
            elif y - 1 >= 0 and mat[x][y - 1] > mat[x][y]:
                y -= 1
            else:
                break
        return [x, y]
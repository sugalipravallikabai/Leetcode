from collections import defaultdict
class Solution:
    def isValidSudoku(self, b : List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sq = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if b[r][c] == '.':
                    continue
                elif b[r][c] in row[r] or b[r][c] in col[c] or b[r][c] in sq[(r//3,c//3)]:
                    return False
                row[r].add(b[r][c])
                col[c].add(b[r][c])
                sq[(r//3,c//3)].add(b[r][c])
        return True
        
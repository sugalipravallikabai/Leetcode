class Solution:
    def countStudents(self, std : List[int], sand: List[int]) -> int:
        
        circle = std.count(1)
        sq = std.count(0)
        for i in range(len(sand)):
            food = sand[i]
            if food == 1:
                if not circle:
                    return sq
                circle -= 1
            else:
                if not sq:
                    return circle
                sq -= 1
        return 0
class Solution:
    def minMovesToSeat(self, seats : List[int], std : List[int]) -> int:
        
        seats.sort()
        std.sort()
        
        n = len(std)
        tol = 0
        for i in range(n):
            tol += abs(seats[i] - std[i])
        return tol
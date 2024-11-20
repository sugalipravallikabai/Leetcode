class Solution:
    def minCostClimbingStairs(self, c : List[int]) -> int:
        d = [0] * len(c)
        d[0] = c[0]
        d[1] = c[1]
        for i in range(2,len(c)):
            take = c[i]+d[i-2]
            nottake = c[i]+d[i-1]
            d[i] = min(take,nottake)
        return min(d[-1],d[-2])
        
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini = float('inf')
        for n in nums:
            val = abs(mini)
            if abs(n) < val:
                mini = n
            elif n == val:
                if n > mini:
                    mini = n
                
                
        return mini
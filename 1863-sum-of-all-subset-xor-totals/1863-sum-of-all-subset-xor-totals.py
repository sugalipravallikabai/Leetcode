
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        x = 0
        for n in nums:
            x |= n
        return x * (1 << (len(nums)-1))
        
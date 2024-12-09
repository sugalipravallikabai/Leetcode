class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d:
                return [d[target - nums[i]],i]
            d[nums[i]] = i
        return [-1,-1]
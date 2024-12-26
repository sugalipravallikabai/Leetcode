class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        mini = min(nums)
        return mini
        # while l <= r:
        #     m = (l+r)//2
        #     if nums[m] == 
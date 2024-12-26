class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        if nums[0] != nums[1] :
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        l,r = 0,n-2
        while l <= r:
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif (m % 2 == 1 and nums[m] == nums[m-1]) or (m % 2 == 0 and nums[m] == nums[m+1])  :
                l = m+1
            else:
                r = m-1
        return -1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        mini = min(nums)
        # return mini
        while l <= r:
            m = (l+r)//2
            if nums[m] == mini:
                return mini
            if nums[l] <= nums[m]:
                if nums[l] <= mini and mini <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[r] >= mini and mini >= nums[m]:
                    l = m+1
                else:
                    r = m-1
        return -1
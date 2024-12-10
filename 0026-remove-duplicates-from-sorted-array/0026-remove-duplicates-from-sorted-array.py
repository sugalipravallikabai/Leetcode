class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
        l,r = 0,1
        while r < len(nums):
            if nums[l] != nums[r]:
                l+=1
                nums[l] = nums[r]
            r += 1
        print(l)
        return l+1
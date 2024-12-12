class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        cnt = 0
        for i in range(len(nums)):
            if k-nums[i] in d and d[k-nums[i]] > 0:
                cnt += 1
                d[k-nums[i]] -= 1
            else:
                d[nums[i]] = d.get(nums[i],0)+1
        return cnt
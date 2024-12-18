from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        same = [0]*2
        diff = [0]*2
        for i in range(n):
            cur = nums[i]%2
            same[cur] = 1+same[cur]
            diff[cur] = max(diff[cur],1+diff[cur^1])
        
        return max(same[0],same[1],diff[0],diff[1])


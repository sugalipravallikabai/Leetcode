class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=set(nums)
        if 0 in n:
            n.remove(0)
        print(n)
        return len(n)
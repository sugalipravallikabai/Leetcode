from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        d = Counter(nums)
        
        repeated = max(d,key=d.get)
        
        return repeated
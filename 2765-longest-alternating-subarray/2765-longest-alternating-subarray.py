class Solution:
    def alternatingSubarray(self, num : List[int]) -> int:
        n = len(num)
        res = dp = -1
        for i in range(1,n):
            if dp > 0 and num[i] == num[i-2]:
                dp += 1
            else:
                dp = 2 if num[i] == num[i-1]+1 else -1
            
            res = max(res,dp)
        return res
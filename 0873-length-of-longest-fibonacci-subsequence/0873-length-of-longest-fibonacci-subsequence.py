from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        
        index = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        dp = defaultdict(int)
        max_len = 0
        
        for i in range(1,n):
            for j in range(i):
                prev = arr[i]- arr[j]
                
                if prev < arr[j] and prev in index:
                    k = index[prev]
                    dp[j,i] = dp.get((k,j),2)+1
                    max_len = max(max_len,dp[j,i])
        return max_len if max_len >= 3 else 0

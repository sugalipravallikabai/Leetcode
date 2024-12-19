from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Store the index of each number in the array for quick lookup
        index = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        
        # DP dictionary to store the length of subsequences ending with arr[i] and arr[j]
        dp = defaultdict(int)
        max_len = 0
        
        # Iterate over all pairs of indices (i, j) with i < j
        for j in range(1, n):
            for i in range(j):
                # Check if arr[i] and arr[j] can form the next Fibonacci number
                prev = arr[j] - arr[i]
                if prev < arr[i] and prev in index:
                    k = index[prev]
                    dp[i, j] = dp.get((k, i), 2) + 1  # If a valid subsequence exists, extend it
                    max_len = max(max_len, dp[i, j])
        
        return max_len if max_len >= 3 else 0  # Fibonacci subsequence must have at least 3 numbers

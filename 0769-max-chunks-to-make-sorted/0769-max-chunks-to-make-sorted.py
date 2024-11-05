class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = 0
        val = arr[0]
        for i in range(len(arr)):
            if val < arr[i]:
                val = arr[i]
            if val == i:
                cnt += 1
        return cnt
class Solution:
    def longestAlternatingSubarray(self, a: List[int], t: int) -> int:
        n = len(a)
        ans = 0
        c = 0  # Length of the current valid subarray
        start = -1  # Start index of the current valid subarray

        for i in range(n):
            if a[i] > t:
                c = 0
                start = -1
            elif a[i] % 2 == 0 and start == -1:
                c = 1
                start = i
            elif start != -1:
                if a[i] % 2 != a[i - 1] % 2:
                    c += 1
                else:
                    if a[i] % 2 == 0:
                        c = 1
                        start = i
                    else:
                        c = 0
                        start = -1
            ans = max(ans, c)
        return ans


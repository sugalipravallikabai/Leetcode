class Solution:
    def longestAlternatingSubarray(self, a : List[int], t : int) -> int:
        
        n = len(a)
        ans = 0
        for i in range(n):
            c = 0
            if a[i] % 2 == 0 and a[i] <= t:
                c = 1

                for j in range(i+1,n):

                    if a[j]%2 == a[j-1]%2 or a[j] > t:
                        break
                    c += 1
            ans = max(ans,c)
        return ans

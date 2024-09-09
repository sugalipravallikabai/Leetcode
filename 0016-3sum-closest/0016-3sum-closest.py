from typing import List

class Solution:
    def threeSumClosest(self, n: List[int], t: int) -> int:
        n.sort()
        ans = float('-inf')
        for i in range(len(n)-2):
            j = i+1
            k = len(n)-1
            while j < k:
                s = n[i]+n[j]+n[k]
                if abs(s-t) < abs(ans-t):
                    ans = s
                if s < t:
                    j += 1
                elif s > t:
                    k -= 1
                else:
                    return ans
        return ans

            
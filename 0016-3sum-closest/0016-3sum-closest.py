from typing import List

class Solution:
    def threeSumClosest(self, n: List[int], t: int) -> int:
        n.sort()  
        closest_sum = float('inf')
        
        for i in range(len(n) - 2):
            j, k = i + 1, len(n) - 1
            while j < k:
                s = n[i] + n[j] + n[k]
                if abs(s - t) < abs(closest_sum - t):
                    closest_sum = s
                
                if s < t:
                    j += 1  
                elif s > t:
                    k -= 1  
                else:
                    return s
        
        return closest_sum

            
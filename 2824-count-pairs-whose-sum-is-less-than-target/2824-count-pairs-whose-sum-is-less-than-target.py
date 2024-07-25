class Solution:
    def countPairs(self, n : List[int], target: int) -> int:
        
        cnt = 0
        n.sort()
        l,r = 0,len(n)-1
        while l < r:
            if n[l] + n[r] < target:
                cnt += r-l
                l += 1
            else:
                r -= 1
        return cnt
        
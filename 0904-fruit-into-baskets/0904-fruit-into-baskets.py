class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        n = len(fruits)
        maxi = 0
        d = {}
        r,l = 0,0
        while r < n:
            if fruits[r]  in d:
                d[fruits[r]] += 1
            else:
                d[fruits[r]] = 1
            if len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
                    
            if len(d) <= 2:
                maxi = max(maxi,r-l+1)
            r += 1
        return maxi
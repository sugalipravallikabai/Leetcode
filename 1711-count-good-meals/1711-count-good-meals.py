from collections import Counter
class Solution:
    def countPairs(self, d : List[int]) -> int:
        cnt = 0
        mod = (10**9) + 7
        n = len(d)
        fre = Counter(d)
        maxi = max(d)*2
        powers = [2**i for i in range(31) if 2**i <= maxi ]
        for num in d:
            fre[num] -= 1
            for pow in powers:
                com = pow - num
                if com in fre and fre[com] > 0:
                    cnt += fre[com]
        return cnt%mod
# import math
class Solution:
    def hasGroupsSizeX(self, d : List[int]) -> bool:
        freq = Counter(d)
        nums = list(freq.values())
        gcd = math.gcd(*nums)
        return gcd != 1
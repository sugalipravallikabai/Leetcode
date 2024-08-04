class Solution:
    def findIntersectionValues(self, n1: List[int], n2: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        for i in n1:
            if i in n2:
                cnt1 += 1
        for j in n2:
            if  j in n1:
                cnt2 += 1
        return [cnt1,cnt2]
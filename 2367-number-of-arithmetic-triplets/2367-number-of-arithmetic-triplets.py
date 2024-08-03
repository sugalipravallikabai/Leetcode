class Solution:
    def arithmeticTriplets(self, n : List[int], d : int) -> int:
        cnt = 0
        for i in n:
            if i+d in n and i-d in n:
                cnt+=1
        return cnt
        
class Solution:
    def majorityElement(self, n : List[int]) -> int:
        ele = 0
        cnt = 0
        for i in range(len(n)):
            if cnt == 0:
                ele = n[i]
                cnt = 1
            elif n[i] == ele :
                cnt += 1
            else :
                cnt -= 1
        return ele
class Solution:
    def isWinner(self, p1: List[int], p2: List[int]) -> int:
        if len(p1) < 2 or len(p2) < 2:
            if sum(p1) > sum(p2):
                return 1
            elif sum(p2) > sum(p1):
                return 2
            return 0
        
        t1 = p1[0]
        if p1[0] == 10 :
            t1 += p1[1] * 2
        else:
            t1 += p1[1] 
        t2 = p2[0]
        if p2[0] == 10 :
            t2 += p2[1] * 2
        else:
            t2 += p2[1] 
        for i in range(2,len(p1)):
            if p1[i-1] == 10 or p1[i-2] == 10:
                t1 += p1[i] * 2
            else:
                t1 += p1[i]
        for j in range(2,len(p2)):
            if p2[j-1] == 10 or p2[j-2] == 10:
                t2 += p2[j] * 2
            else:
                t2 += p2[j] 
        if t1 > t2:
            return 1
        if t2 > t1:
            return 2
        return 0
class Solution:
    def validMountainArray(self, a : List[int]) -> bool:
        flag = 0
        if len(a) <= 2:
            return False
        if a[0] > a[1]:
            return False
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                return False
            if a[i] > a[i+1]:
                flag = 1
            if flag == 1 and a[i] < a[i+1]:
                return False
        if flag == 1:
            return True
        return False
        
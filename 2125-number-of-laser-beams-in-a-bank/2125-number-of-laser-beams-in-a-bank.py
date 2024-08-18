class Solution:
    def numberOfBeams(self, b : List[str]) -> int:
        temp = []
        tol = 0
        for i in b:
            x = i.count('1')
            if x != 0:
                temp.append(x)
        if len(temp) == 1:
            return 0
        for i in range(len(temp)-1):
            tol += temp[i]*temp[i+1]
        return tol 
        
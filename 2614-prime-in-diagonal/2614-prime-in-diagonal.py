from math import sqrt
class Solution:
    def diagonalPrime(self, n : List[List[int]]) -> int:
        
        d1 = []
        maxi = 0
        for i in range(len(n)):
            for j in range(len(n[0])):
                if i - j == 0:
                    d1.append(n[i][j])
                elif i+j == len(n)-1:
                    d1.append(n[i][j])
        for val in d1:
            if val == 1:
                maxi = 0
            elif val <= 3:
                maxi = max(maxi,val)
                continue
            flag = 0
            for i in range(2,int(math.sqrt(val))+1):
                if val % i == 0:
                    flag = 1
                    break
            if flag == 0 and val != 1:
                maxi = max(maxi,val)
        return maxi
            
        
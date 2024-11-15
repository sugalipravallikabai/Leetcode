class Solution:
    def rotate(self, a : List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(a)):
            for j in range(i+1,len(a[0])):
                if i != j:
                    a[i][j],a[j][i] = a[j][i],a[i][j]
        for i in range(len(a)):
            a[i].reverse()
        return a
        
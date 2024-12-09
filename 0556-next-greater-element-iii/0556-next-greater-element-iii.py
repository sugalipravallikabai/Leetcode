class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = [int(val) for val in str(n)]
        ind = -1
        size = len(l)
        for i in range(size-2,-1,-1):
            if l[i] < l[i+1]:
                ind = i
                break
        if ind == -1:
            return -1
        for i in range(size-1,-1,-1):
            if l[ind] < l[i]:
                l[ind],l[i]=l[i],l[ind]
                break
        l[ind+1:] = sorted(l[ind+1:])
        num = int(''.join(map(str,l)))
        if num <= (2**31)-1:
            return num
        return -1
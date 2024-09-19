class Solution(object):
    def fourSum(self, n , t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n.sort()
        a = []
        k = 0
        l = len(n)-1
        for i in range(len(n)):
            if i > 0 and n[i] == n[i-1]:
                continue
            for j in range(i+1,len(n)):
                if j > i+1 and n[j] == n[j-1]:
                    continue
                k = j+1
                l = len(n)-1
                while k < l:
                    s = n[i]+n[j]+n[k]+n[l]
                    if s == t:
                        a.append([n[i],n[j],n[k],n[l]])
                        while k < l and n[k] == n[k+1]: k += 1
                        while k < l and n[l] == n[l-1]: l -= 1
                        k += 1
                        l -= 1
                    elif s < t:
                        k += 1
                    else:
                        l -= 1
        return a
        
class Solution:
    def arrayStringsAreEqual(self, w1: List[str], w2: List[str]) -> bool:
        t = ""
        t1 = ""
        for i in range(len(w1)):
            t += w1[i]
        for j in range(len(w2)):
            t1 += w2[j]
        return t == t1
        
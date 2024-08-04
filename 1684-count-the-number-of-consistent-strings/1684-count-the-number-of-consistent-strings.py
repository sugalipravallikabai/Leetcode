class Solution:
    def countConsistentStrings(self, a : str, w : List[str]) -> int:
        cnt = 0
        a = set(a)
        for i in w:
            if all(c in a for c in i):
                cnt+=1
        return cnt
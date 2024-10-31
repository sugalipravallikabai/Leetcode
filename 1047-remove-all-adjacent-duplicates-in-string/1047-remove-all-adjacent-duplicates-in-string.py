class Solution:
    def removeDuplicates(self, s: str) -> str:
        t = []
        for c in s:
            if t and t[-1] == c:
                t.pop()
            else:
                t.append(c)
        return ''.join(t)
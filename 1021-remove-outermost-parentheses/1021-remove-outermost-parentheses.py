class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        t = []
        x = 0
        for c in s:
            if c == ')':
                x -= 1
            if x > 0:
                t.append(c)
            if c == '(':
                x += 1
        return ''.join(t)
class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        cnt = 0
        # st = []
        for c in s:
            if c == '(':
                cnt += 1
                m = max(m,cnt)
            if c == ')':
                cnt -= 1
        return m
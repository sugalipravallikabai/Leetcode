class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                val = max(2*st.pop(),1)
                st[-1] += val
        return st[-1]
        
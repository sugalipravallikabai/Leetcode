class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fun(s):
            st = []
            for c in s:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return ''.join(st)
        return fun(s) == fun(t)
            
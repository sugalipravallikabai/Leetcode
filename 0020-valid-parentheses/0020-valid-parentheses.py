class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '([{':
                st.append(c)
            else:
                if not st:
                    return False
                chr = st[-1]
                if (c == ')' and chr == '(') or (c == ']' and chr == '[') or (c == '}' and chr == '{'):
                    st.pop()
                else:
                    return False
        return False if st else True
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if st and c in '1234567890':
                st.pop()
            else:
                st.append(c)
        return ''.join(st)
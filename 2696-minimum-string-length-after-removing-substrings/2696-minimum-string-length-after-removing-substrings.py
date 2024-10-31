class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for c in s:
            if st and c == 'B' and st[-1] == 'A':
                st.pop()
            elif st and c == 'D' and st[-1] == 'C':
                st.pop()
            else:
                st.append(c)
        return len(st)
            
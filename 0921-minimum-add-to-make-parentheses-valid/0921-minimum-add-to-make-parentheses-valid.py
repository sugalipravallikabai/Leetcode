class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        cnt = 0
        for c in s:
            if c == '(':
                st.append(c)
            else:
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(c)
                    cnt+=1
        return len(st)
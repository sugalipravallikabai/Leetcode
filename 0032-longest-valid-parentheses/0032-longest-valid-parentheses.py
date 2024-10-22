class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        st = [-1]
        m = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                x = st.pop()
                if len(st) == 0:
                    st.append(i)
                m =max(m,i-st[-1])
        return m
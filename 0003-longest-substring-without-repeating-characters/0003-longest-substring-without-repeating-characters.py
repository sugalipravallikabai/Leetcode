class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        m = 0
        for c in s:
            if c not in st:
                st.append(c)
            else:
                while c in st:
                    st.pop(0)
                st.append(c)
            m = max(m,len(st))
        return m
            
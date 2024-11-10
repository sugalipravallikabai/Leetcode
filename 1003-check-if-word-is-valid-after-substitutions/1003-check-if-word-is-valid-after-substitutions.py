class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            st.append(i)
            if len(st) > 2 and ''.join(st[-3:]) == 'abc':
                st.pop()
                st.pop()
                st.pop()
        # print(st[-3:])
        return len(st) == 0
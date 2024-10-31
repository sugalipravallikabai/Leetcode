class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for c in s:
            if st and ((ord(st[-1])-32 == ord(c)) or (ord(st[-1])+32 == ord(c))):
                st.pop()
            else:
                st.append(c)
        return ''.join(st)
class Solution:
    def calPoints(self, op: List[str]) -> int:
        st = []
        for i in op:
            if i == 'C':
                st.pop()
            elif i == 'D':
                x = st[-1]
                st.append(x*2)
            elif i == '+':
                x,y = st[-1],st[-2]
                st.append(x+y)
            else:
                st.append(int(i))
        return sum(st)
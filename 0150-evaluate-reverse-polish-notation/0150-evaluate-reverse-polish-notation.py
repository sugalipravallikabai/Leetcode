class Solution:
    def evalRPN(self, t : List[str]) -> int:
        st = []
        for v in t:
            if v.lstrip('-').isdigit():
                st.append(int(v))
            else:
                x2 = st.pop()
                x1 = st.pop()
                if v == '+':
                    st.append(x1+x2)
                elif v == '*':
                    st.append(x2*x1)
                elif v == '-':
                    st.append(x1-x2)
                elif v == '/':
                    st.append(int(x1/x2))
        return sum(st)
                    
                    
                    
class Solution:
    def evalRPN(self, t : List[str]) -> int:
        st = []
        for i in t:
            if i.lstrip('-').isdigit():
                st.append(int(i))
            else:
                n1 = st.pop()
                n2 = st.pop()
                if i == '+':
                    tol = n1+n2
                elif i == '-':
                    tol = n2-n1
                elif i == '*':
                    tol = n2 * n1
                else:
                    tol = int(n2/n1)
                st.append(tol)
                
        return st[-1]
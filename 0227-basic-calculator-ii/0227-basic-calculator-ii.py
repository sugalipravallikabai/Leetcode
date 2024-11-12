import math
class Solution:
    def calculate(self, s: str) -> int:
        pre = '+'
        n = 0
        st = []
        for c in s+'+':
            if c.isdigit():
                n = n * 10 + int(c)
            elif c in '+-*/':
                if pre == '+':
                    st.append(n)
                elif pre == '-':
                    st.append(-n)
                elif pre == '*':
                    st.append(st.pop()*n)
                elif pre == '/':
                    st.append(math.trunc(st.pop()/n))
                pre = c
                n = 0
                
        return sum(st)
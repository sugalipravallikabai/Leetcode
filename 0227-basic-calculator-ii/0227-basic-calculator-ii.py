class Solution:
    def calculate(self, s: str) -> int:
        pre = '+'
        num = 0
        st = []
        for c in s+'+':
            if c.isdigit():
                num = num*10+int(c)
            elif c in '+-*/':
                if pre == '+':
                    st.append(num)
                elif pre == '-':
                    st.append(-num)
                elif pre == '*':
                    st.append(st.pop()*num)
                elif pre == '/':
                    st.append(math.trunc(st.pop()/num))
                pre = c
                num = 0
        return sum(st)
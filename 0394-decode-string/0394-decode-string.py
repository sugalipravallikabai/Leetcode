class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        ans = ''
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c == '[':
                st.append(num)
                st.append(ans)
                ans,num = '',0
            elif c == ']':
                pre_str = st.pop()
                pre_num = st.pop()
                ans = pre_str+ans*pre_num
            else:
                ans+=c
        return ans
            
        
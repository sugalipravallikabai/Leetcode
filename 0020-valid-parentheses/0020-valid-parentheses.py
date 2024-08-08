class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        
        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                chr = st.pop()
                if chr == '(' and i != ')':
                    return False
                if chr == '[' and i != ']':
                    return False
                if chr == '{' and i != '}':
                    return False
                
        return len(st) == 0
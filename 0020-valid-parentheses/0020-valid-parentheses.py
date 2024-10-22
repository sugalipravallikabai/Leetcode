class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '({[':
                st.append(c)
            elif c in ')}]':
                if not st:
                    return False
                x = st.pop()
                if (x == '(' and c != ')') or (x == '[' and c != ']') or (x == '{' and c != '}'):
                    return False
        
        return True if len(st)==0 else False
class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        p = path.split('/')
        # print(p)
        for c in p:
            if st and c == '..':
                st.pop()
            elif c not in ['','..','.']:
                st.append(c)
        # print(st)
        return '/'+'/'.join(st)
                         
        
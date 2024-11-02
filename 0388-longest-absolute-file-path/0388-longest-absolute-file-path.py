class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        ans = 0
        st = [0]
        for path in paths:
            p = path.split('\t')
            dpt,name = len(p)-1,p[-1]
            while len(st) > dpt+1 :
                st.pop()
            if '.' in name:
                ans = max(ans,st[-1]+len(name))
            else:
                st.append(st[-1]+len(name)+1)
        return ans
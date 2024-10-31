class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for c in logs:
            if st and c == '../':
                st.pop()
            if c not in ['../','./']:
                st.append(c)
        return len(st)
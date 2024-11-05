class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        st = []
        for c in logs:
            log = c.split(':')
            print(log)
            if log[1] == 'start':
                st.append(log)
            else:
                val = st.pop()
                ind = int(val[0])
                res = int(log[2]) - int(val[2]) +1
                ans[ind] += res
                if st:
                    x = int(st[-1][0])
                    ans[x] -= res
        
        return ans
        
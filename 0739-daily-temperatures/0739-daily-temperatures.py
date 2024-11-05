class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        ans = [0]*len(t)
        st = []
        for i in range(len(t)-1,-1,-1):
            while st and t[st[-1]] <= t[i]:
                st.pop()
            if st and t[st[-1]] > t[i]:
                ans[i] = st[-1]-i
            st.append(i)
        return ans
                    
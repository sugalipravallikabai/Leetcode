class Solution:
    def maxSlidingWindow(self, n : List[int], k: int) -> List[int]:
        l = []
        st = deque()
        for i in range(len(n)):
            if st and st[0] <= i-k:
                st.popleft()
            while st and n[st[-1]] <= n[i]:
                st.pop()
            st.append(i)
            if i >= k-1:
                l.append(n[st[0]])
        return l
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        ans = [-1]*n
        for i in range(2*n-1,-1,-1):
            while st and st[-1] <= nums[i%n]:
                st.pop()
            if st:
                ans[i%n] = st[-1]
            st.append(nums[i%n])
        return ans
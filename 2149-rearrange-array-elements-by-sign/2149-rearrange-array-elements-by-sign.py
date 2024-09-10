class Solution:
    def rearrangeArray(self, n : List[int]) -> List[int]:
        pos = []
        neg = []
        ans = [0]*len(n)
        for i in range(len(n)):
            if n[i] > 0:
                pos.append(n[i])
            else:
                neg.append(n[i])
        print(pos)
        for i in range((len(pos))):
            ans[2*i] = pos[i]
            ans[(2*i)+1] = neg[i]
        return ans
            
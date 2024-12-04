class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        lsum,rsum,msum = 0,0,0
        if n <= k:
            return sum(cardPoints)
        lsum = sum(cardPoints[:k])
        msum = lsum
        for i in range(1,k+1):
            lsum -= cardPoints[k-i]
            rsum += cardPoints[-i]
            # print(rsum+lsum)
            msum = max(msum,rsum+lsum)
        return msum
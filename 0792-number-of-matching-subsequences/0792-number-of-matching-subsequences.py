class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def fun(k):
            ind = -1
            for c in k:
                ind = s.find(c,ind+1)
                if ind == -1:
                    return False
            return True
        
        cnt = 0
        for word in words:
            if fun(word):
                cnt += 1
        return cnt
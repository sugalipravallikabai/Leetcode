class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        i = 0
        for c in order:
            d[c] = i
            i+=1
        for j in range(1,len(words)):
            
            for k in range(min(len(words[j]),len(words[j-1]))):
                if d[words[j-1][k]] > d[words[j][k]]:
                    return False
                elif d[words[j-1][k]] < d[words[j][k]]:
                    break
            else:
                if len(words[j-1]) > len(words[j]):
                    return False
            
        return True
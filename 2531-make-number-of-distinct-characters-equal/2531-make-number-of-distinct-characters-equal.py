class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for ch1 in c1:
            for ch2 in c2:
                new_c1 = c1 - Counter({ch1: 1}) + Counter({ch2: 1})
                new_c2 = c2 + Counter({ch1: 1}) - Counter({ch2: 1})
                if len(new_c1) == len(new_c2): 
                    return True
        return False
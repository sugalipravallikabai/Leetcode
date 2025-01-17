class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        for i in range(len(word)):
            s = set()
            if word[i] in 'aeiou':
                for j in range(i,len(word)):
                    if word[j] in 'aeiou':
                        s.add(word[j])
                        if len(s) >= 5:
                            cnt += 1
                    else:
                        break
            else:
                i = i+1
        return cnt
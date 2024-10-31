class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch not in word:
            return word
        res = list(word)
        for i in range(len(res)):
            if res[i] == ch:
                res[:i+1] = res[i::-1]
                return ''.join(res)
        return word
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        cnt = 0
        bannedWords = set(bannedWords)
        for word in message:
            if word in bannedWords:
                cnt += 1
            if cnt == 2:
                return True
        return False
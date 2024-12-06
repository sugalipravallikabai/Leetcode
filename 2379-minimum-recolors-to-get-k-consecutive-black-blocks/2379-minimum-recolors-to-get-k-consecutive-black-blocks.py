class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = float('inf')
        for i in range(len(blocks)-k+1):
            val = blocks[i:i+k].count('W')
            cnt = min(cnt,val)
        return cnt
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cnt = 0
        for op in operations:
            if op == '++X' or op == 'X++':
                cnt += 1
            else:
                cnt -=1
        return cnt
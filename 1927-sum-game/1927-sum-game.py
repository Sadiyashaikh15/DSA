class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        qDiff = 0

        for i in range(half):
            if num[i] == '?':
                qDiff += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                qDiff -= 1
            else:
                diff -= int(num[i])

        if qDiff % 2 != 0:
            return True

        return diff != -9 * (qDiff // 2)
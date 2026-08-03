class Solution:
    def stoneGameIII(self, stoneValue):
        from functools import lru_cache

        n = len(stoneValue)

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            take = 0
            best = float('-inf')

            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    best = max(best, take - dfs(i + k + 1))

            return best

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        return "Tie"
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        positions = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                positions.append(i)
                digits.append(int(ch))

        n = len(digits)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefix_num = [0] * (n + 1)
        for i in range(n):
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(positions, l)
            right = bisect_right(positions, r)

            if left == right:
                ans.append(0)
                continue

            length = right - left

            x = (
                prefix_num[right]
                - prefix_num[left] * pow10[length]
            ) % MOD

            digit_sum = prefix_sum[right] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans
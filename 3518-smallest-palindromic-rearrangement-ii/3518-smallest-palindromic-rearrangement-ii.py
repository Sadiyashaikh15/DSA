from collections import Counter
from math import gcd

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        cnt = Counter(s)

        mid = ""
        half = {}

        total = 0
        for ch in sorted(cnt):
            if cnt[ch] % 2:
                mid = ch
            half[ch] = cnt[ch] // 2
            total += half[ch]

        def comb_cap(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            if r == 0:
                return 1

            ans = 1
            for i in range(1, r + 1):
                num = n - r + i
                den = i
                g = gcd(num, den)
                num //= g
                den //= g

                g = gcd(ans, den)
                ans //= g
                den //= g

                ans *= num
                ans //= den

                if ans > LIMIT:
                    return LIMIT
            return ans

        def count(freq):
            rem = sum(freq.values())
            ans = 1
            left = rem

            for ch in sorted(freq):
                f = freq[ch]
                if f:
                    ans *= comb_cap(left, f)
                    if ans > LIMIT:
                        return LIMIT
                    left -= f
            return ans

        if count(half) < k:
            return ""

        first = []

        while total:
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                if half.get(ch, 0) == 0:
                    continue

                half[ch] -= 1

                ways = count(half)

                if ways >= k:
                    first.append(ch)
                    total -= 1
                    break
                else:
                    k -= ways
                    half[ch] += 1

        first = "".join(first)
        return first + mid + first[::-1]
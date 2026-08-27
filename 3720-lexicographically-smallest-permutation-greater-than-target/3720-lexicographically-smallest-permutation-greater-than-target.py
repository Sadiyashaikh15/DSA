class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        prefix = []
        ans = ""

        for i in range(len(s)):
            target_idx = ord(target[i]) - ord('a')

            # Find smallest available character greater than target[i]
            for j in range(target_idx + 1, 26):
                if freq[j] > 0:
                    freq[j] -= 1

                    suffix = []
                    for k in range(26):
                        suffix.append(chr(k + ord('a')) * freq[k])

                    candidate = (
                        ''.join(prefix)
                        + chr(j + ord('a'))
                        + ''.join(suffix)
                    )

                    if ans == "" or candidate < ans:
                        ans = candidate

                    freq[j] += 1
                    break

            # Match target[i] if possible
            if freq[target_idx] == 0:
                break

            prefix.append(target[i])
            freq[target_idx] -= 1

        return ans
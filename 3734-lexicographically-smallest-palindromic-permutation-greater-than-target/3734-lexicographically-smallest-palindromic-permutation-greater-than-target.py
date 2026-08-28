from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        n = len(s)
        
        # Validate odd character count
        odd_chars = [ch for ch, cnt in freq.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_len = n // 2
        half_freq = Counter({ch: count // 2 for ch, count in freq.items()})
        
        def build_palindrome(left_half: str) -> str:
            return left_half + mid_char + left_half[::-1]

        best_res = None

        def backtrack(curr_half: str):
            nonlocal best_res
            
            # Prune search space: if current prefix is already smaller than target prefix, stop
            idx = len(curr_half)
            if idx > 0 and curr_half < target[:idx]:
                return
            
            # Base case: full left half formed
            if idx == half_len:
                cand = build_palindrome(curr_half)
                if cand > target:
                    if best_res is None or cand < best_res:
                        best_res = cand
                return

            # Explore character choices in sorted order
            for ch in sorted(half_freq.keys()):
                if half_freq[ch] > 0:
                    half_freq[ch] -= 1
                    backtrack(curr_half + ch)
                    half_freq[ch] += 1
                    
                    # If a valid larger palindrome has been found while prefix > target[:idx+1],
                    # we can break early as remaining branches will yield larger palindromes.
                    if best_res is not None and curr_half + ch > target[:idx + 1]:
                        break

        backtrack("")
        return best_res if best_res else ""
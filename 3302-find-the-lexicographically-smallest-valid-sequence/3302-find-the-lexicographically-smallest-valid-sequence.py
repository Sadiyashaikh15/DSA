from bisect import bisect_right
from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # Precompute rightmost matching positions for word2's suffixes
        last = [-1] * (m + 1)
        last[m] = n
        
        ptr = m - 1
        for i in range(n - 1, -1, -1):
            if ptr >= 0 and word1[i] == word2[ptr]:
                last[ptr] = i
                ptr -= 1
                
        # Store character indices for fast binary searching
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(word1):
            pos[ord(ch) - ord('a')].append(i)
            
        result = []
        prev_idx = -1
        used_change = False
        
        for i in range(m):
            chosen_j = -1
            
            if used_change:
                # Must match word2[i] exactly and leave room for word2[i+1...m-1]
                c = ord(word2[i]) - ord('a')
                idx = bisect_right(pos[c], prev_idx)
                if idx < len(pos[c]) and pos[c][idx] < last[i + 1]:
                    chosen_j = pos[c][idx]
            else:
                # Candidate 1: Try smallest possible index (prev_idx + 1)
                candidate = prev_idx + 1
                if candidate < n and candidate < last[i + 1]:
                    chosen_j = candidate
                    if word1[chosen_j] != word2[i]:
                        used_change = True
                else:
                    # Candidate 2: Must match word2[i] exactly
                    c = ord(word2[i]) - ord('a')
                    idx = bisect_right(pos[c], prev_idx)
                    if idx < len(pos[c]):
                        chosen_j = pos[c][idx]
            
            if chosen_j == -1:
                return []
                
            result.append(chosen_j)
            prev_idx = chosen_j
            
        return result
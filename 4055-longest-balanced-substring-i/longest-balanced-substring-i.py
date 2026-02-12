class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = [0] * 26
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                
                # Collect non-zero frequencies
                values = [f for f in freq if f > 0]
                
                # Check balanced condition
                if values and min(values) == max(values):
                    ans = max(ans, j - i + 1)
        
        return ans


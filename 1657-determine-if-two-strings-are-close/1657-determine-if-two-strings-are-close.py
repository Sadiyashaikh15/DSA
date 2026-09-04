from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # Different lengths cannot be close
        if len(word1) != len(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Both strings must contain the same characters
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # Frequency values must match
        return sorted(count1.values()) == sorted(count2.values())
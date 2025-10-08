class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        
        n = len(spells)
        m = len(potions)
        
        pairs = [0] * n
        for i in range(n):
            spell_strength = spells[i]
            
          
            required_strength = (success + spell_strength - 1) // spell_strength
            
            idx = bisect.bisect_left(potions, required_strength)
            
            
            pairs[i] = m - idx
            
        return pairs
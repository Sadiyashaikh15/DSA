class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        while x < n:
            x = (x << 1) | 1   # Multiply by 2 and add 1 → generates next number with all bits set
        return x
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        # Initialize the first two steps
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
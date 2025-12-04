class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        n = len(directions)
        
        # 1. Remove leading L's (they never collide)
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        
        # 2. Remove trailing R's (they never collide)
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # 3. Count all non-stationary cars in the middle segment
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
        
        return collisions

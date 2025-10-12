class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        
        farthest_reachable = 0
        for i in range(n):
       
            if i > farthest_reachable:
                return False
            
        
            farthest_reachable = max(farthest_reachable, i + nums[i])
            
           
            if farthest_reachable >= n - 1:
                return True
                
        
        return True





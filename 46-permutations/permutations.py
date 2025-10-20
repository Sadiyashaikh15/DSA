class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start):
            # Base case: one permutation complete
            if start == len(nums):
                result.append(nums[:])  # append a copy
                return
            
            for i in range(start, len(nums)):
                # Swap current index with start
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # Backtrack (undo swap)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result
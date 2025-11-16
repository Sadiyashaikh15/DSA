class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        jumps = 0
        farthest = 0      # initialize BEFORE using it
        current_end = 0

        # we don't need to process the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # when we've scanned to the end of the current range,
            # we must take a jump (unless we're already at the last index)
            if i == current_end:
                jumps += 1
                current_end = farthest

                # optional early exit: if current_end already reaches or passes last index
                if current_end >= len(nums) - 1:
                    break

        return jumps

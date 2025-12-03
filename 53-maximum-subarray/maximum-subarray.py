class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current = 0
        for num in nums:
            current += num
            max_sum = max(max_sum, current)
            if current < 0:
                current = 0
        return max_sum
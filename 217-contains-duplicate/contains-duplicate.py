class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen_numbers = set()
        for num in nums:
            if num in seen_numbers:
                return True
            else:
                seen_numbers.add(num)
        return False
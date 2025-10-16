class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        remainder_count = defaultdict(int)
        for num in nums:
            # Calculate non-negative remainder
            remainder = num % value
            remainder_count[remainder] += 1
        
        # Start checking from 0 upwards to find the smallest non-negative integer not present
        x = 0
        while True:
            # Calculate the remainder of x when divided by value
            r = x % value
            # If there's a number that can be adjusted to x (i.e., has remainder r)
            if remainder_count[r] > 0:
                remainder_count[r] -= 1
                x += 1
            else:
                return x
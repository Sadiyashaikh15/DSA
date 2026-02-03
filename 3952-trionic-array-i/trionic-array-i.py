class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        i = 0

        # 1️⃣ strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i >= n - 2:
            return False

        # 2️⃣ strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i >= n - 1:
            return False

        # 3️⃣ strictly increasing again
        inc = False
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
            inc = True

        return inc and i == n - 1

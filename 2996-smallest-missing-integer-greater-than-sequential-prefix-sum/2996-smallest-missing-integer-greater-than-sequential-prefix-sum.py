class Solution:
    def missingInteger(self, nums):
        total = nums[0]

        # Find sum of longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find smallest missing integer >= total
        while total in nums:
            total += 1

        return total
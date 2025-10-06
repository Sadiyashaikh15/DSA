class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1]*n
        for i in range(1, n):
            answer[i] = nums[i-1]*answer[i-1]
        R_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i]*R_product
            R_product = R_product*nums[i]
        return answer
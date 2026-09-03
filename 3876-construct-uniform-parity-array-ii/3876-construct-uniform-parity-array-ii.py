class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        for num in nums1:
            if num % 2== 1:
                return mn % 2 == 1
        return True
class Solution:
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)

        while mx:
            mn, mx = mx, mn % mx

        return mn
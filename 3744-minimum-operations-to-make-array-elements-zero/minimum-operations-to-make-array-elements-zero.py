class Solution(object):
    def f_sum(self, n):
        """
        Helper function: total 'divide by 4' steps for numbers 1..n
        Each number x takes floor(log4(x)) + 1 steps to reduce to 0
        """
        if n == 0:
            return 0
        total = 0
        power = 1  # 4^0
        k = 0
        while power * 4 <= n:
            next_power = power * 4
            total += (next_power - power) * (k + 1)  # full range of numbers in this power of 4
            power = next_power
            k += 1
        total += (n - power + 1) * (k + 1)  # remaining numbers
        return total

    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        ans = 0
        for l, r in queries:
            # Total cost in this query's range
            cost = self.f_sum(r) - self.f_sum(l - 1)
            # Each operation reduces 2 numbers, so divide by 2 and ceil
            ans += (cost + 1) // 2
        return ans
 
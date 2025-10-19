class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, current, total):
            # Base cases
            if total == target:
                res.append(list(current))
                return
            if total > target:
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # not i+1 because reuse allowed
                current.pop()  # backtrack step

        backtrack(0, [], 0)
        return res
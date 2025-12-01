class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total = sum(batteries)
        lo, hi = 1, total // n    
        def can(run):
            required = n * run
            available = 0
            for b in batteries:
                available += min(b, run)
                if available >= required:
                    return True
            return False
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
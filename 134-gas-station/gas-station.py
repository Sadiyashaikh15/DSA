class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_diff = 0
        curr = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_diff += diff
            curr += diff

            # If we fail here, restart from next station
            if curr < 0:
                curr = 0
                start = i + 1

        # If total gas < total cost → cannot complete
        return start if total_diff >= 0 else -1
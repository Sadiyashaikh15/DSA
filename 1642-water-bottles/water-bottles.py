class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk_bottles =numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            new_bottles_from_exchange = empty_bottles // numExchange
            total_drunk_bottles +=new_bottles_from_exchange
            empty_bottles = (empty_bottles % numExchange)+new_bottles_from_exchange
        return total_drunk_bottles
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk_bottles = numBottles
        empty_bottles = numBottles
        
       
        while empty_bottles >= numExchange:
            # Perform one exchange
            total_drunk_bottles += 1  # Drink one new bottle
            empty_bottles -= numExchange # Use numExchange empty bottles
            empty_bottles += 1 # The newly drunk bottle becomes empty
            numExchange += 1 # The exchange rate increases by one
            
        return total_drunk_bottles






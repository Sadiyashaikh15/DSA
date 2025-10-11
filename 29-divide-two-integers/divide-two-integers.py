class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

       
        is_negative = (dividend < 0) ^ (divisor < 0)

        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            while (temp_divisor << 1) <= abs_dividend:
                temp_divisor <<= 1
                multiple <<= 1
        
            abs_dividend -= temp_divisor
            quotient += multiple
        if is_negative:
            quotient = -quotient
        if quotient > MAX_INT:
            return MAX_INT
        

        if quotient < MIN_INT:
            return MIN_INT
            
        return int(quotient)
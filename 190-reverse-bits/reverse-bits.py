class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):          # process all 32 bits
            bit = n & 1              # take last bit
            result = (result << 1) | bit   # add it to result (from left side)
            n >>= 1                  # remove last bit
        
        return result

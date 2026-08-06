class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.digit_product(n) % t == 0:
                return n
            n += 1

    def digit_product(self, num: int) -> int:
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        return product
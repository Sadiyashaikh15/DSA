class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # If rows = 1, no zigzag happens
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr = 0          # current row index
        direction = -1    # used to flip direction

        for ch in s:
            rows[curr] += ch

            # change direction at the top or bottom row
            if curr == 0 or curr == numRows - 1:
                direction *= -1

            curr += direction

        return "".join(rows)

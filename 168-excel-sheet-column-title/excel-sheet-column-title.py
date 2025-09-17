class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            result = chr(ord('A') + remainder) + result
            columnNumber = (columnNumber - 1) // 26
        return result
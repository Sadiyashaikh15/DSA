class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(1, n):
            i = 0
            new_s = ""
            while i < len(s):
                count = 1
                # Count identical consecutive digits
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                new_s += str(count) + s[i]
                i += 1
            s = new_s
        return s
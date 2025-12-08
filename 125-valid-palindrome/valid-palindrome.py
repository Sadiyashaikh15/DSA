class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean == clean[::-1]
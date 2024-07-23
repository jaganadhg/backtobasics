import re

class Solution:
    def isPalindrome(self, astring: str) -> bool:
        if len(astring) <= 1:
            return True
        clean_str = re.sub(r'[^A-Za-z0-9]', '', astring.lower()).replace(' ', '')
        return clean_str == clean_str[::-1]


"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
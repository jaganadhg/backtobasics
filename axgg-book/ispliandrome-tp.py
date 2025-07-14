"""
Check if a given string is
a palindrome using two pointers.
"""


def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome using two pointers.

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    test_strings = ["Malayalam"]
    for s in test_strings:
        print(f"Is '{s}' a palindrome? {is_palindrome(s)}")

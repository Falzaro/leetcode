from typing import Counter


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    counter = Counter(s)
    odd = 0
    for val in counter.values():
        if val % 2 == 1:
            odd += 1
    return len(s) - odd + 1 if odd > 0 else len(s)
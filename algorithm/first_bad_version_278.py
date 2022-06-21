"""
Example 1:
Input: n = 5, bad = 4
Output: 4

Example 2:
Input: n = 1, bad = 1
Output: 1
"""
# def isBadVersion API is already defined for you
# def isBadVersion(version: int) -> bool

def isBadVersion(version):
    return False

def firstBadVersion(self, n: int) -> int:
    low, high = 1, n
    while low <= high:
        mid = (high - low) // 2 + low
        print(low, high, mid)
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low
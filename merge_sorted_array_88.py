"""
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
"""
def merge(nums1, m, nums2, n):
    last = m + n - 1
    # Note: it's m > 0 and not m >= 0 because we did not decrement m.
    while m > 0 and n > 0:
        if nums2[n - 1] > nums1[m - 1]:
            nums1[last] = nums2[n - 1]
            n -= 1
        else:
            nums1[last] = nums1[m - 1]
            m -= 1
        last -= 1
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1
    return nums1

result = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)  # Output: [1, 2, 3, 4, 5, 6]
print(result)

# result = merge([1], 1, [], 0)  # Output: [1, 2, 3, 4, 5, 6]
# print(result)

result = merge([1, 4, 7, 0, 0, 0], 3, [0, 2, 8], 3)  # Output: [0, 1, 2, 4, 7, 8]
print(result)


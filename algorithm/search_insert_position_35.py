"""
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

You must write an algorithm with O(log n) runtime complexity
"""

# def searchInsert(nums, target):
#     i = 0
#     while i < len(nums):
#         if nums[i] >= target:
#             return i
#         i += 1
#     return i

def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r - l) // 2 + l
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l

result = searchInsert([1, 3, 5, 6], 5)
print(result)
result = searchInsert([1, 3, 5, 6], 2)
print(result)
result = searchInsert([1, 3, 5, 6], 7)
print(result)
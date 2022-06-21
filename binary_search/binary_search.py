"""
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        # mid = (low + high) // 2
        mid = (high - low) // 2 + low
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def search_r(nums, low, high, target):
    mid = (high - low) // 2 + low
    if low > high:
        return -1
    elif target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return search_r(nums, mid + 1, high, target)
    else:
        return search_r(nums, low, mid - 1, target)

# search([-1, 0, 3, 5, 9, 12], 13)
nums = [-1, 0, 3, 5, 9, 12]
result = search_r(nums, 0, len(nums) - 1, 3)
print(result)
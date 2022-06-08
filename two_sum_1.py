"""
Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
"""

def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if num not in lookup:
            lookup[complement] = i
        else:
            return [i, lookup[num]]

result = twoSum([2, 7, 11, 15], 9)
print(result)
result = twoSum([3, 2, 4], 6)
print(result)

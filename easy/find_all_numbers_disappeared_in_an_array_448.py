"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
n = 8
Output: [5, 6]

temp = 1
[4, 3, 2, 7, 8, 2, 3, 1]

Example 2:
Input: nums = [1, 1]
Output: [2]
"""

# With hash set
def findDisappearedNumbersHashSet(nums):
    hashSet = set()
    output = []
    for num in nums:
        hashSet.add(num)
    for i in range(1, len(nums) + 1):
        if i not in hashSet:
            output.append(i)
    print(output)

def findDisappearedNumbers(nums):
    for num in nums:
        while num != -1:
            temp = nums[num - 1]
            nums[num - 1] = -1
            num = temp

    i, p = 0, 0
    while i < len(nums):
        if nums[i] != -1:
            nums[p] = i + 1 
            p += 1
        i += 1 
    print(nums[0:p])

findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
findDisappearedNumbers([1, 1])


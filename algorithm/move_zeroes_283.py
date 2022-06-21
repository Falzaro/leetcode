"""
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def moveZeroes(nums):
    i, j = 0, 0
    while j < len(nums):
        if nums[j] is not 0: 
            nums[i], nums[j] = nums[j], nums[i]
            i +=1
        j += 1
    print(nums)

moveZeroes([0, 1, 0, 3, 12])
moveZeroes([0])
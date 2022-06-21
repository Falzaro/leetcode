"""
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

[0, 1, 9, 16, 100]
[0, 1, 9, 16, 100]

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

[4, 9, 9, 49, 121]
"""

def sortedSquares(nums):
    l, r = 0, len(nums) - 1
    res = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res.append(nums[l]**2) 
            l += 1
        else:
            res.append(nums[r]**2)
            r -= 1
    return res[::-1]

result = sortedSquares([-4, -1, 0, 3, 10])
print(result)
result = sortedSquares([-7, -3, 2, 3, 11])
print(result)
# result = sortedSquares([-5, -3, -2, -1]) # [1, 4, 9, 25]
# print(result)
# result = sortedSquares([-4, -1, 0, 3, 10]) # [1, 4, 9, 25]
# print(result)

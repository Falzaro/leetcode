"""
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

def reverseNums(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    

def rotate(nums, k):
    k = k % len(nums)
    reverseNums(nums, 0, len(nums)-1)
    print(nums)
    reverseNums(nums, 0, k - 1)
    print(nums)
    reverseNums(nums, k, len(nums)-1)
    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)
# rotate([-1], 2)
# rotate([-1, -100, 3, 99], 2)
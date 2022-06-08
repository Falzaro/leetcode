def maxSubArray(nums):
    maxSum = float("-inf")
    subSum = float("-inf")
    for num in nums:
        subSum = max(subSum + num, num)
        maxSum = max(maxSum, subSum)
    return maxSum


result = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # Output: [4, -1, 2, 1] sum: 6
result = maxSubArray([1, -5, 3, -1, -1, 3, -4])  # Output: [4, -1, 2, 1] sum: 6
print(result)

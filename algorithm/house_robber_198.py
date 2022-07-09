"""
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

def rob(nums):
    prev, prev_prev = 0, 0
    for num in nums:
        temp = max(prev_prev + num, prev)
        prev_prev = prev
        prev = temp
    return prev


# print(rob([0])) # 1 + 3 = 4
print(rob([1, 2, 3, 1])) # 1 + 3 = 4
print(rob([2, 7, 9, 3, 1])) # 2 + 9 + 1 = 12
print(rob([10, 1, 1, 20, 10])) # 10 + 20 = 30 
print(rob([10, 1, 1, 20, 30, 2, 15]))

"""

first = 1
second = 2
temp = 



"""
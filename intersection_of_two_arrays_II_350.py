from collections import Counter
"""
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

# Hashmap approach
def intersect_hashmap(nums1, nums2):
    c = Counter(nums2)
    output = []
    for num in nums1:
        if num in c and c[num] > 0: 
            output.append(num)
            c[num] -= 1

    return output
            
def intersect_sorted(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    i, j = 0, 0
    output = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            output.append(nums1[i])
            i += 1
            j += 1

    return output

# result = intersect_hashmap([1, 2, 2, 1], [2, 2])
# print(result)
# result = intersect_hashmap([4, 9, 5], [9, 4, 9, 8, 4])
# print(result)

result = intersect_sorted([1, 2, 2, 1], [2, 2])
print(result)
result = intersect_sorted([4, 9, 5], [9, 4, 9, 8, 4])
print(result)
# Remove values from a list
def removeValues(nums, values):
    p = 0
    for num in nums:
        if num not in values:
            nums[p] = num
            p += 1
    print(nums[:p])

print(removeValues([5, 1, 4, 1, 7], {5, 1}))
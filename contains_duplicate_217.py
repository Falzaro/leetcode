def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# example [4, 1, 2, 1]
def another_containsDuplicate(nums):
    hash_table = {}
    for num in nums:
        if num not in hash_table:
            hash_table[num] = 1
        else:
            return True
    return False

print(another_containsDuplicate([4, 1, 2, 1]))

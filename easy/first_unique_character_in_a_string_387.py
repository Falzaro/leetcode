"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

[l, o, v, e]

Example 3:
Input: s = "aabb"
Output: -1
"""

def firstUniqChar(s):
    output = -1
    # Put unique characters into a queue
    queue = []
    # Use a set to check for repeated characters
    lookup = {}
    for i, c in enumerate(s):
        if c not in lookup:
            queue.append(c)
            lookup[c] = i
        else:
            lookup[c] = -1
    for c in queue:
        if lookup[c] != -1:
            return lookup[c]
    return output

# result = firstUniqChar("leetcode")
# print(result)
# result = firstUniqChar("loveleetcode")
# print(result)
# result = firstUniqChar("aabb")
# print(result)

def firstUniqueCharBest(s):
    hashTable = {}
    for c in s:
        hashTable[c] = hashTable.get(c, 0) + 1
    for i in range(len(s)):
        if hashTable[s[i]] == 1:
            return i
    return -1

result = firstUniqueCharBest("leetcode")
print(result)
result = firstUniqueCharBest("loveleetcode")
print(result)
result = firstUniqueCharBest("aabb")
print(result)

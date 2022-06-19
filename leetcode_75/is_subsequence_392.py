"""
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

def isSubsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t): 
        if s and s[i] == t[j]:
            i += 1
        j += 1
    return i >= len(s)

result = isSubsequence("abc", "ahbgdc")
print(result)
result = isSubsequence("axc", "ahbgdc")
print(result)
result = isSubsequence("", "ahbgdc")
print(result)
result = isSubsequence("b", "abc")
print(result)
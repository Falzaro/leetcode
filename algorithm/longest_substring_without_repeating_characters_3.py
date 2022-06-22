"""
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s) -> int:
    hs = set()
    maxLen = 0
    for i, c in enumerate(s):
        j = i - len(hs)
        if c not in hs:
            hs.add(c)
        elif s[j] != c:
            while s[j] != c:
                hs.remove(s[j])
                j += 1
        maxLen = max(maxLen, len(hs))
    print(maxLen)


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")
lengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring(" ")
lengthOfLongestSubstring("ohvhjdml")
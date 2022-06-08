"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""

def maxNumberOfBalloons(text):
    ht = {
        'b': 0,
        'a': 0,
        'l': 0,
        'o': 0,
        'n': 0
    }
    for c in text:
        if c in ht:
            ht[c] += 1
    ht['l'] //= 2
    ht['o'] //= 2
    return min(ht.values())

"""
Test cases
"""
result = maxNumberOfBalloons("nlaebolko")
print(result)
result = maxNumberOfBalloons("loonbalxballpoon")
print(result)
result = maxNumberOfBalloons("leetcode")
print(result)
result = maxNumberOfBalloons("balllllllllllloooooooooon")
print(result)
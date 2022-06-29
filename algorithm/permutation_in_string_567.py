"""
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

Other test cases:
Input: s1 = "adc", s2 = "dcda"
Output: true
"""

from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    ht1, ht2 = {}, {}
    for i in range(26):
        ht1[chr(97+i)] = 0
        ht2[chr(97+i)] = 0
    for i, c in enumerate(s1):
        ht1[c] += 1
        ht2[s2[i]] += 1 
    if ht1 == ht2:
        return True
    for i in range(len(s1), len(s2)):
        ht2[s2[i]] += 1
        ht2[s2[i-len(s1)]] -= 1
        if ht1 == ht2:
            return True
    return False

    
    

# print(checkInclusion("ab", "eidbaooo"))
# print(checkInclusion("ab", "eidboaoo"))
print(checkInclusion("adc", "dcda"))
# print(checkInclusion("adc", "dbcad"))
# print(checkInclusion("hello", "ooolleooholeh"))
# print(checkInclusion("cab", "dbabcd"))

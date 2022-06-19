"""
Example  1:
Input: s = "egg", t = "add"
Output: true
{ e: a, g: d }
e, g, g
==
a, d, d
e -> a == t[i] (a)

Example  2:
Input: s = "foo", t = "bar"
Output: false
f -> b == t[i]
o -> a == t[i] (r)

Example  3:
Input: s = "paper", t = "title"
Output: true
Input: s = "badc", t = "baba"
Output: false
"""

def isIsomorphic(s, t):
    mapST = {}
    setT = set()
    for c1, c2 in zip(s, t):
        if c1 not in mapST:
            mapST[c1] = c2
            if c2 in setT:
                return False
            setT.add(c2)
        else:
            if mapST[c1] != c2:
                return False
    return True

def isIsomorphicNeet(s, t):
    mapST = {}
    mapTS = {}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True


result = isIsomorphic("egg", "add")
print(result)
result = isIsomorphic("foo", "bar")
print(result)
result = isIsomorphic("paper", "title")
print(result)
result = isIsomorphic("badc", "baba")
print(result)
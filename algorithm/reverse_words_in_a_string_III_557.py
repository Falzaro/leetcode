"""
Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""

# def reverseWords(s):
#     res = ""
#     word = ""
#     for l in s:
#         if l == " ":
#             res = res + word + l
#             word = ""
#         else:
#             word = l + word
#     return res + word

# def reverseWords(s):
#     res = []
#     word = ""
#     for l in s:
#         if l == " ":
#             res.append(word)
#             word = ""
#         else:
#             word = l + word
#     res.append(word)
#     print(" ".join(res))

def reverseWords(s):
    res = []
    words = s.split()
    for word in words:
        res.append(word[::-1])
    return " ".join(res)


print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))

"""
hello world
olleh 
"""
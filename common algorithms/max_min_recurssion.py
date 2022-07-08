""" Tail recursion approach"""
def maxNum(arr):
    return arr[0] if len(arr) == 1 else max(arr.pop(), maxNum(arr))

def minNum(arr):
    return arr[0] if len(arr) == 1 else min(arr.pop(), minNum(arr))

arr = [1, 4, 3, -5, -4, 8, 6]
print(maxNum(arr.copy())) # max = 8
print(minNum(arr.copy())) # max = 8
print(maxNum(arr)) # max = 8
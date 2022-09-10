arr = [1, 2, 3, 4, 5]

def reverseArr(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
reverseArr(arr)
print(arr)
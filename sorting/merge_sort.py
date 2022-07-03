def merge(arrayOne, arrayTwo):
    merged = []
    i, j = 0, 0
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] < arrayTwo[j]:
            merged.append(arrayOne[i])
            i +=1
        else:
            merged.append(arrayTwo[j])
            j += 1
    if i < len(arrayOne):
        merged.extend(arrayOne[i:])
    if j < len(arrayTwo):
        merged.extend(arrayTwo[j:])
    return merged

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2

    arrayOne = mergeSort(arr[:mid])
    arrayTwo = mergeSort(arr[mid:])

    return merge(arrayOne, arrayTwo)

print(mergeSort([5, 1, 2, 3, 4, 0, -1]))
# print(mergeSort([]))
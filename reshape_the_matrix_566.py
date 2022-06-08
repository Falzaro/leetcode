"""
Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""
def matrixReshape(mat, r, c):
    # Check if the reshape operation is legal
    if len(mat) * len(mat[0]) != r * c:
        return mat

    # Fill the reshaped matrix with r x c of zeroes
    reshaped_mat = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(0)
        reshaped_mat.append(row)

    i, j = 0, 0
    # flatten the matrix into a one-dimensional array and then assign each element of it
    # to the corresponding entry of the reshaped matrix
    for rows in mat:
        for num in rows:
            if j == c:
                i += 1
                j = 0
            reshaped_mat[i][j] = num
            j += 1
    return reshaped_mat

result = matrixReshape([[1, 2], [3, 4]], 1, 4)
print(result)
result = matrixReshape([[1, 2], [3, 4]], 2, 4)
print(result)
"""
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""

def generate(numRows):
    output = [[1]]
    for _ in range(1, numRows):
        l, r = -1, 0
        row = []
        prevRow = output[-1]
        while l < len(prevRow):
            if l < 0 or r == len(prevRow):
                row.append(1)
            else:
                row.append(prevRow[l] + prevRow[r])
            l, r = l + 1, r + 1
        output.append(row) 
    return output

def generate_neetcode(numRows):
    output = [[1]]
    for _ in range(numRows - 1):
        row = []
        temp = [0] + output[-1] + [0]
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        output.append(row)
    return output

result = generate(5)
print(result)

result = generate_neetcode(5)
print(result)
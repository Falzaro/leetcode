nums = [5, 2, 1, 2]

def square(n):
    return n*n

squared_nums = list(map(square, nums))
squared_nums_lambda = list(map(lambda n : n*n, nums))
print(squared_nums_lambda)
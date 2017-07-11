def count_paths(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    row = num_rows - 1
    col = num_cols - 1

    memo = [[0 for j in range(num_cols)] for i in range(num_rows)]

    while row >= 0:
        col = num_cols - 1
        while col >= 0:
            if grid[row][col]:
                if row == num_rows - 1 and col == num_rows - 1:
                    # if bottom right, memoize 1 path
                    memo[row][col] = 1
                elif row == num_rows - 1:
                    # if bottom row, only look right
                    memo[row][col] = memo[row][col + 1]
                elif col == num_cols - 1:
                    # if rightmost column, only look down
                    memo[row][col] = memo[row + 1][col]
                else:
                    # for all other squares sum the squares to left and right
                    memo[row][col] = memo[row + 1][col] + memo[row][col + 1]
            else:
                memo[row][col] = 0
            col -= 1

        row -= 1

    return memo[0][0]


a = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]


b = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]


c = [
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 1]
]

print count_paths(a) == 6
print count_paths(b) == 2
print count_paths(c) == 4

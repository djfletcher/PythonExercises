def count_paths(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    # create new grid of same dimensions to memoize number of paths from each square
    memo = [[0 for j in range(num_cols)] for i in range(num_rows)]

    # start at bottom right and work our way back to origin row by row
    row = num_rows - 1
    while row >= 0:
        col = num_cols - 1
        while col >= 0:
            if grid[row][col]:
                # if current square is a 1 then memoize num paths from this square
                if row == num_rows - 1 and col == num_rows - 1:
                    # initialize bottom  1 path
                    memo[row][col] = 1
                elif row == num_rows - 1:
                    # if bottom row, the only path is to the right
                    memo[row][col] = memo[row][col + 1]
                elif col == num_cols - 1:
                    # if rightmost column, the only path is down
                    memo[row][col] = memo[row + 1][col]
                else:
                    # sum the squares currently below and to the right
                    memo[row][col] = memo[row + 1][col] + memo[row][col + 1]
            else:
                # if current square is a 0, then memoize that there are 0 paths from this square
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

# Given two strings, return the minimum number of edits to turn str1 into str2

def minimum_edit_distance(str1, str2):
    memo = [[]]
    for str1_idx in range(len(str1)):
        for str2_idx in range(len(str2)):
            if str1_idx == 0:
                memo[str1_idx].append(0 if str1[str1_idx] == str2[str2_idx] else 1)
            elif str2_idx == 0:
                memo.append([0] if str1[str1_idx] == str2[str2_idx] else [1])
            else:
                if str1[str1_idx] == str2[str2_idx]:
                    memo[str1_idx].append(memo[str1_idx - 1][str2_idx - 1])
                else:
                    memo[str1_idx].append(1 + min(
                    memo[str1_idx][str2_idx - 1],
                    memo[str1_idx - 1][str2_idx],
                    memo[str1_idx - 1][str2_idx - 1]
                    ))
    return memo[len(str1) - 1][len(str2) - 1]

# print(minimum_edit_distance('abc', 'abb') == 1)
# print(minimum_edit_distance('mob', 'moby') == 1)
# print(minimum_edit_distance('abc', 'def') == 3)
# print(minimum_edit_distance('hope', 'open') == 2)


# Find largest square submatrix
def max_submatrix(matrix):
    memo = [[0] * len(matrix[0]) for i in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == 0 or col == 0:
                memo[row][col] = 0
            elif matrix[row][col] == 0:
                memo[row][col] = 0
            else:
                memo[row][col] = 1 + min(
                    memo[row][col - 1],
                    memo[row - 1][col - 1],
                    memo[row - 1][col]
                )
    max = 0
    for row in memo:
        for val in row:
            if val > max:
                max = val
    return max

test1 = [
  [1, 0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1]
]

test2 = [
  [1, 0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 1, 1],
  [1, 1, 1, 1, 0, 1]
]

test3 = [
  [1, 0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1]
]

test4 = [[]]

test5 = [
  [0, 1, 1],
  [0, 0, 1],
  [0, 1, 1]
]

print(max_submatrix(test1) == 4)
print(max_submatrix(test2) == 3)
print(max_submatrix(test3) == 2)
print(max_submatrix(test4) == 0)
print(max_submatrix(test5) == 1)



def print_spiral(matrix):
    # set top, right, bottom, and left boundaries to zero and length of matrix
    # peel off each layer, breaking if there are no layers left, and
    # readjust the boundaries, moving them in each time
    top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
    result = []
    while len(result) < len(matrix) * len(matrix[0]):
        # top
        if bottom < top:
            break
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # right
        if right < left:
            break
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # bottom
        if bottom < top:
            break
        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1

        # left
        if right < left:
            break
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][left])
        left += 1
    return result

test1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

test2 = [
  [1,  2,  3,  4,  5,  6],
  [7,  8,  9,  10, 11, 12],
  [13, 14, 15, 16, 17, 18]
]

test3 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]

print(print_spiral(test1) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(print_spiral(test2) == [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11])
print(print_spiral(test3) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

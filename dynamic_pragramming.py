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

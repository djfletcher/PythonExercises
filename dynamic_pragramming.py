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

print(minimum_edit_distance('abc', 'abb') == 1)
print(minimum_edit_distance('mob', 'moby') == 1)
print(minimum_edit_distance('abc', 'def') == 3)
print(minimum_edit_distance('hope', 'open') == 2)

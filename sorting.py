def bubblesort(lst):
    dup = lst[:]
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if dup[j] > dup[j + 1]:
                dup[j], dup[j + 1] = dup[j + 1], dup[j]
    return dup

print('# Bubblesort')
print(bubblesort([4,6,1,88,3]) == [1,3,4,6,88])
print(bubblesort([4,3,2,1]) == [1,2,3,4])
print(bubblesort([1,2,3]) == [1,2,3])


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = len(lst) / 2
    left, right = [], []

    switch = {
        -1: lambda x: left.append(x),
        0: lambda x: left.append(x),
        1: lambda x: right.append(x)
    }

    for i, val in enumerate(lst):
        if i == pivot:
            continue
        switch[cmp(val, lst[pivot])](val)

    return quicksort(left) + [lst[pivot]] + quicksort(right)


print('# Quicksort')
print(quicksort([4,6,1,88,3]) == [1,3,4,6,88])
print(quicksort([4,3,2,1]) == [1,2,3,4])
print(quicksort([1,2,3]) == [1,2,3])

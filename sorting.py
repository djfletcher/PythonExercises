def bubblesort(lst):
    dup = lst[:]
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if dup[j] > dup[j + 1]:
                dup[j], dup[j + 1] = dup[j + 1], dup[j]
    return dup

print '# Bubblesort'
print bubblesort([4,6,1,88,3]) == [1,3,4,6,88]
print bubblesort([4,3,2,1]) == [1,2,3,4]
print bubblesort([1,2,3]) == [1,2,3]


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


print '# Quicksort'
print quicksort([4,6,1,88,3]) == [1,3,4,6,88]
print quicksort([4,3,2,1]) == [1,2,3,4]
print quicksort([1,2,3]) == [1,2,3]



def mergesort(lst):
    if len(lst) <= 1:
        return lst
    pivot = len(lst) / 2

    left = mergesort(lst[:pivot])
    right = mergesort(lst[pivot:])

    return merge(left, right)

def merge(left, right):
    merged = []
    switch = {
        -1: lambda: merged.append(left.pop(0)),
        0: lambda: merged.append(left.pop(0)),
        1: lambda: merged.append(right.pop(0))
    }

    while left and right:
        switch[cmp(left[0], right[0])]()

    return merged + left + right


print '# Mergesort'
print mergesort([4,6,1,88,3]) == [1,3,4,6,88]
print mergesort([4,3,2,1]) == [1,2,3,4]
print mergesort([1,2,3]) == [1,2,3]



def bsearch(lst, target):
    if not lst:
        return None

    pivot = len(lst) / 2

    if lst[pivot] < target:
        return bsearch(lst[:pivot], target)
    elif lst[pivot] == target:
        return pivot
    else:
        result = bsearch(lst[pivot + 1:], target)
        return None if not result else result + 1


print '# Binary Search'
print bsearch([1,2,3,4,5,6,7,8,9,10], 4) == 3
print bsearch([1,2,3,4,5,6,7,8,9,10], -2) == None
print bsearch([1,2,3,4,5,6,7,8,9,10], 11) == None
print bsearch([1,2,3,4,5,6,7,8,9,10], 10) == 9

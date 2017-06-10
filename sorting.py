def bubblesort(lst):
    dup = lst[:]
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if dup[j] > dup[j + 1]:
                dup[j], dup[j + 1] = dup[j + 1], dup[j]
    return dup


print(bubblesort([4,6,1,88,3]) == [1,3,4,6,88])
print(bubblesort([4,3,2,1]) == [1,2,3,4])
print(bubblesort([1,2,3]) == [1,2,3])

# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/#/description
def findMedianSortedArrays(nums1, nums2):
    length = (len(nums1) + len(nums2))
    if length % 2 == 0:
        median_indices = [length // 2 - 1, length // 2]
    else:
        median_indices = [length // 2]

    merged = []
    while len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] <= nums2[0]:
            merged.append(nums1.pop(0))
        else:
            merged.append(nums2.pop(0))

    merged = merged + nums1 + nums2
    total = 0
    for i in median_indices:
        total += merged[i]
    return total / len(median_indices)

print(findMedianSortedArrays([1,3], [2]) == 2)
print(findMedianSortedArrays([1,3], [2,5]) == 2.5)
print(findMedianSortedArrays([1,3], [2,5,7]) == 3)

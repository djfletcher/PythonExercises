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


# Source: https://leetcode.com/problems/add-two-numbers/#/description
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    num1, num2 = fromLinkToInt(l1), fromLinkToInt(l2)
    return fromIntToLink(num1 + num2)

def fromLinkToInt(link):
    num = 0
    multiplier = 1
    while link:
        num += multiplier * link.val
        link = link.next
        multiplier *= 10
    return num

def fromIntToLink(num):
    divisor = 1
    head = None
    prev = None
    while num > 0:
        digit = num % (divisor * 10)
        link = ListNode(digit // divisor)
        num -= digit
        if head is None:
            head = link
        if prev:
            prev.next = link
        prev = link
        divisor *= 10
    return head

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
d.next = e
e.next = f

res = addTwoNumbers(a, d)
print(res.val is 7 and res.next.val is 0 and res.next.next.val is 8)

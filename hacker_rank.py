# Source: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
def ransom_note(magazine, ransom):
    mag_words = {}
    for word in magazine:
        if word not in mag_words:
            mag_words[word] = 1
        else:
            mag_words[word] += 1

    for word in ransom:
        if word not in mag_words or mag_words[word] is 0:
            return False
        else:
            mag_words[word] -= 1
    return True


# Source: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen
# Node is defined as
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# Given a root node, check whether it is a valid Binary Search Tree
def checkBST(root, mini=None, maxi=None):
    if not root or not root.left and not root.right:
        return True
    if mini and mini >= root.data or maxi and maxi <= root.data:
        return False
    return checkBST(root.left, mini, root.data) and checkBST(root.right, root.data, maxi)



def  degreeOfArray(arr):
# Iterate through array and keep count of how many times each element appears, using a dict
# Dict should point to another dict with three keys:
    # 1. Count
    # 2. First Index
    # 3. Last Index
    memo = {}
    for idx, element in enumerate(arr):
        memoize(element, idx, memo)
    degree = 0
    minimum_length = float('inf')
    for element in memo:
        count = memo[element]['count']
        subarray_length = memo[element]['last_idx'] + 1 - memo[element]['first_idx']
        print("num: {}, count: {}, sub_length: {}".format(element, count, subarray_length))
        if count >= degree and subarray_length < minimum_length:
            degree = count
            minimum_length = subarray_length
    return minimum_length



def memoize(element, idx, memo):
    if element not in memo:
        memo[element] = {
            'count': 1,
            'first_idx': idx,
            'last_idx': idx
        }
    else:
        memo[element]['count'] += 1
        memo[element]['last_idx'] = idx




def searchNodes(root, target, hops=0):
# modified DFS:
    if root is None:
        return None
    # 1. check if root's val is target; if so return hops
    if root.value == target:
        return hops
    # 2. if not, then check if root's val is greater than target; if so, return hops (or None)
    elif root.value > target:
        return None
    # 3. if not, then recurse on right and below nodes.
    else:
        next_result = searchNodes(root.next, target, hops + 1)
        below_result = searchNodes(root.below, target, hops + 1)
        if next_result is None and below_result is None:
            return hops
        elif next_result is None:
            return below_result
        elif below_result is None:
            return next_result
        else:
            return next_result if next_result < below_result else below_result



# Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
#
# A Node is defined as:
#
#     class Node(object):
#         def __init__(self, data = None, next_node = None):
#             self.data = data
#             self.next = next_node

def has_cycle(head):
    seen = set()
    node = head
    while node.next:
        if node in seen:
            return True
        seen.add(node)
        node = node.next
    return False

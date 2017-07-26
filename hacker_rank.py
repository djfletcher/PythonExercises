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
def check(root, min, max):
    if root is None:
        return True
    elif root.data <= min or root.data >= max:
        return False
    else:
        return check(root.left, min, root.data) and check(root.right, root.data, max)

def checkBST(root):
    return check(root, float('-inf'), float('inf'))



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


# Source: https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(')')
        elif char == '{':
            stack.append('}')
        elif char == '[':
            stack.append(']')
        else:
            if len(stack) == 0 or stack.pop(-1) != char:
                return False
    return len(stack) == 0

a = []
print(a.pop(-1))



# Source: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
        try:
            return self.stack2[-1]
        except IndexError:
            return None

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
        try:
            return self.stack2.pop(-1)
        except IndexError:
            return None


    def put(self, value):
        self.stack1.append(value)

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

# A BST (Binary Search Tree) Implementation
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----------------------------------- #

def find(tree, val):
    if tree is None:
        return False
    if tree.val == val:
        return True    
    # If the current node's value is less than the target value, search the right subtree
    elif tree.val < val:
        return find(tree.right, val)    
    # If the current node's value is greater than the target value, search the left subtree
    else:
        return find(tree.left, val)
    
# ----------------------------------- #

def insert(tree, val):
    if tree is None:
        return Node(val)
    if tree.val < val:
        tree.right = insert(tree.right, val)
    elif tree.val > val:
        tree.left = insert(tree.left, val)
    return tree

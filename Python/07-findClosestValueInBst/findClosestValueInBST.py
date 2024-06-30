# Find Closest Value In BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    return bst_helper(tree, target, float('inf'))

def bst_helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return bst_helper(tree.right, target, closest)
    else:
        return closest

# Function to insert values into the BST
def insert_into_bst(tree, value):
    if tree is None:
        return BST(value)
    if value < tree.value:
        tree.left = insert_into_bst(tree.left, value)
    else:
        tree.right = insert_into_bst(tree.right, value)
    return tree

# Create a BST and insert values
root = BST(10)
insert_into_bst(root, 5)
insert_into_bst(root, 2)
insert_into_bst(root, 5)
insert_into_bst(root, 1)
insert_into_bst(root, 15)
insert_into_bst(root, 13)
insert_into_bst(root, 22)
insert_into_bst(root, 14)

# Call the findClosestValueInBst function
target = 12
closest_value = findClosestValueInBst(root, target)
print(f"The closest value to {target} in the BST is {closest_value}")

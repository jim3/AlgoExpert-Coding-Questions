# ------------branch_sums------------ #

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if not node:
        return []
    return [node.value] + pre_order_traversal(node.left) + pre_order_traversal(node.right)

def branch_sums(root):
    if root is not None:
        print(root.val) # "root": "1"
        branch_sums(root.left)
        branch_sums(root.right)
    pass

# --------------------------------------------- #
# Uses pre-order traversal which visits the current node first, 
# then the left subtree, and finally the right subtree.
"""
{
  "nodes": [
    { "id": "1", "left": "2", "right": "3", "value": 1 },
    { "id": "2", "left": "4", "right": "5", "value": 2 },
    { "id": "3", "left": "6", "right": "7", "value": 3 },
    { "id": "4", "left": "8", "right": "9", "value": 4 },
    { "id": "5", "left": "10", "right": null, "value": 5 },
    { "id": "6", "left": null, "right": null, "value": 6 },
    { "id": "7", "left": null, "right": null, "value": 7 },
    { "id": "8", "left": null, "right": null, "value": 8 },
    { "id": "9", "left": null, "right": null, "value": 9 },
    { "id": "10", "left": null, "right": null, "value": 10 }
  ],
  "root": "1"
}
"""